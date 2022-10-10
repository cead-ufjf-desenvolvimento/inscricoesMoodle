from django import forms
from FormApp.models import Curso, DadosDoAluno
from django.utils import timezone
from localflavor.br.forms import BRCPFField

class AlunosForm(forms.ModelForm):
    possui_siape = forms.BooleanField(required=False, label="Possui SIAPE?", initial=False, widget=forms.Select(attrs={'class': 'form-select'}, choices=((False, "Não"), (True, "Sim"))))
    
    curso = forms.ModelChoiceField(queryset=Curso.objects.all().order_by('nome'), widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = DadosDoAluno
        fields = '__all__'
        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Somente números'}),
            'data_nascimento': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primeiro nome ou nome social'}),
            'sobrenome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Último nome'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail válido (necessário para confirmação de matrícula)'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Somente números'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Somente números'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ex.: apartamento 101'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.Select(attrs={'class': 'form-select'}),
            'siga': forms.Select(choices=((False, "Não"), (True, "Sim")), attrs={'class': 'form-select'}),
            'siape': forms.TextInput(attrs={'class': 'form-control', 'style': 'display: none;'}),
            'documentacao': forms.FileInput(attrs={'class': 'form-control'}),
        }

class CursosForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = "__all__"
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo do curso'}),
            'nome_breve': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: DIS123-' + str(timezone.now().year) + '.1-A'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'data_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'matricula_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'matricula_fim': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'anexar_documentacao': forms.Select(attrs={'class': 'form-select'}, choices=((False, "Não"), (True, "Sim"))),
        }