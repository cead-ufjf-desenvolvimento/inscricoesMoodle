import csv, json, os

from django.shortcuts import render
from django.views.generic.edit import CreateView
from FormApp.forms import AlunosForm
from FormApp.utils import PasswdGen, SendEmail
from FormApp.models import DadosDoAluno

# Create your views here.
class CadastroAlunoCreateView(CreateView):
    form_class = AlunosForm
    template_name = 'form_aluno.html'
    success_url = '/thanks'
    
    def form_valid(self, form):
        new_data = form.save(commit=False)
        # Atualização dos dados com máscara para que contenham apenas numerais
        new_data.telefone = form.cleaned_data['telefone'].replace('(', '').replace(')', '')
        new_data.cpf = form.cleaned_data['cpf'].replace('.', '').replace('-', '')
        new_data.cep = form.cleaned_data['cep'].replace('-', '')
        new_data.telefone = form.cleaned_data['telefone'].replace('(', '').replace(')', '').replace(' ', '')
        new_data.save()
        
        self.request.session['dados_aluno'] = new_data.id

        # Criação do nome do arquivo com base nos dados do curso
        data_matricula = form.cleaned_data['curso'].matricula_inicio.strftime('%d%m%y')
        nome = form.cleaned_data['curso'].nome
        nome_breve = form.cleaned_data['curso'].nome_breve
        filename = 'outputs/' + nome + '_' + data_matricula

        # Atualização dos campos do dicionário para a formatação de interesse 
        form.cleaned_data['curso'] = form.cleaned_data['curso'].nome
        form.cleaned_data['data_nascimento'] = form.cleaned_data['data_nascimento'].strftime('%d%m%y')
        form.cleaned_data['cpf'] = form.cleaned_data['cpf'].replace('.', '').replace('-', '')
        form.cleaned_data['telefone'] = form.cleaned_data['telefone'].replace('(', '').replace(')', '').replace(' ', '')
        
        
        ### JSON ###
        # Verificação para o caso de já existirem alunos cadastrados no curso em questão
        try:
            with open(filename + '.json') as f:
                listObj = json.load(f)
        except:
            listObj = []
        listObj.append(form.cleaned_data)

        # Conversão dos dados para json
        cleaned_data_json = json.dumps(listObj, indent=4, ensure_ascii=False)
        # Escrita do json
        with open(filename + '.json', 'w') as f:
            f.write(cleaned_data_json)

        ### CSV ###
        # Criação de um dicionário com cabeçalho adequado
        pwd = PasswdGen()
        new_data = {
            'username': form.cleaned_data['cpf'],
            'password': pwd.run(),
            'firstname': form.cleaned_data['nome'],
            'lastname': form.cleaned_data['sobrenome'],
            'email': form.cleaned_data['email'],
            'city': form.cleaned_data['cidade'],
            'auth': 'manual',
            'course1': nome_breve,
        }

        # Verificação para o caso de já existirem alunos cadastrados no curso em questão
        try:
            with open(filename + '.csv', 'r') as f:
                if f.readline().split(',')[0] == 'username':
                    flag = True
                else:
                    flag = False
        except:
            flag = False
            
        # Escrita do arquivo .csv
        with open(filename + '.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=list(new_data.keys()))
            if not flag:
                writer.writeheader()
            writer.writerows([new_data])

        ### MYSQL ###
        # Escrita do arquivo MySQL
        with open(filename + '_mysql.sql', 'a') as f:
            f.write('INSERT INTO {{TABLE}}.{{SGDB}} ' + str(tuple(new_data.keys())) + ' ')
            f.write('VALUES ' + str(tuple(new_data.values())) + ';\n')

        ### SQL ###
        with open(filename + '_postgresql.sql', 'a') as f:
            f.write('INSERT INTO {{TABLE}}.{{SGDB}}' + str(tuple(new_data.keys())) + ' ')
            f.write('VALUES ' + str(tuple(new_data.values())) + ';\n')
        f.close()

        ### SEND EMAIL ###
        subject = "CEAD | UFJF - Orientações para Acesso à Plataforma Moodle"
        
        message = """
        Prezado(a),

        Bem-vindo(a) ao Cead UFJF!
        Em breve você será inscrito(a) no curso {}. 
        Ao final das inscrições, para acessar sua conta na plataforma Moodle, verifique as informações abaixo:

        Acesse: http://ead.cead.ufjf.br (ao final do período de inscrição)
        Identificação: {}
        Senha: {}

        Em caso de dúvidas referentes à plataforma, entre em contato com suporte.cead@ufjf.br
        Para demais informações, entre em contato com a coordenação do curso.

        Atenciosamente,
        SAUT - Serviço de Atendimento ao Usuário
        Coordenação Tecnológica - CEAD | UFJF

        """.format(form.cleaned_data['curso'], new_data['username'], new_data['password'])

        recipients = [new_data['email']]

        new_email = SendEmail(subject=subject, message=message, recipients=recipients)
        new_email.send()

        return super().form_valid(form)

def thanks(request):
    dados_aluno = DadosDoAluno.objects.get(pk=request.session['dados_aluno'])
    context = {'dados_aluno': dados_aluno}
    return render(request, 'thanks.html', context)