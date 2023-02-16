from django.db import models
from localflavor.br.br_states import STATE_CHOICES

from FormApp.validators import validateBirthdate, validateCPF, validatePDF

# Create your models here.
class Curso(models.Model):
    CATEGORIA_CHOICES = (
        ('SIGA/UAB', 'Correspondência no SIGA/UAB'),
        ('SIGA/Flex', 'Correspondência no SIGA/Flexibilização Curricular'),
        ('Livre', 'Sem Correspondência no SIGA/Curso Livre')
    )

    nome = models.CharField(max_length=255)
    nome_breve = models.CharField(max_length=31, verbose_name="Nome Breve")
    categoria = models.CharField(max_length=9, choices=CATEGORIA_CHOICES)
    data_inicio = models.DateField(verbose_name="Início das Atividades")
    data_fim = models.DateField(verbose_name="Fim das Atividades")
    matricula_inicio = models.DateTimeField(verbose_name="Início das Inscrições")
    matricula_fim = models.DateTimeField(verbose_name="Fim das Inscrições")
    ativo = models.BooleanField(default=True)
    
    anexar_documentacao = models.BooleanField(verbose_name="Anexar Documentação", default=False, null=True, blank=True)


    def __str__(self):
        return self.nome

class DadosDoAluno(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name="Curso Pretendido")
    documentacao = models.FileField(verbose_name="Documentação", upload_to="uploads", blank=True, null=True, validators=[validatePDF])

    cpf = models.CharField(max_length=14, verbose_name="CPF", validators=[validateCPF])
    data_nascimento = models.DateField(verbose_name="Data de Nascimento", validators=[validateBirthdate])
    nome = models.CharField(
        max_length=63, 
        verbose_name="Nome/Nome Social", 
        help_text="""Em caso de nome social, é necessário que o mesmo conste em documento emitido pela 
            Receita Federal ou Instituto de Identificação para emissão do certificado de conclusão/participação com nome social.
            Em caso de dúvidas, procure os canais de atendimento da Receita Federal. 
        """)
    sobrenome = models.CharField(max_length=127)
    email = models.EmailField(verbose_name="e-mail")
    cidade = models.CharField(max_length=63)

    telefone = models.CharField(max_length=15)
    cep = models.CharField(max_length=9, verbose_name="CEP")
    logradouro = models.CharField(max_length=255, verbose_name="Logradouro")
    numero = models.IntegerField(verbose_name="Número")
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=31)
    uf = models.CharField(max_length=2, verbose_name="UF", choices=STATE_CHOICES)
    
    siga = models.BooleanField(verbose_name="É aluno da UFJF?")
    siape = models.CharField(max_length=7, null=True, blank=True, verbose_name="SIAPE")

    data_cadastro = models.DateTimeField(auto_now_add=True)