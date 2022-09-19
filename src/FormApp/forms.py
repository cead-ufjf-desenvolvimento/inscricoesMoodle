from django import forms
from FormApp.models import DadosDoAluno
from localflavor.br.forms import BRCPFField

class AlunosForm(forms.ModelForm):
    possui_siape = forms.BooleanField(required=False, label="Possui SIAPE?", initial=False, widget=forms.Select(attrs={'class': 'form-select'}, choices=((False, "Não"), (True, "Sim"))))
    
    class Meta:
        model = DadosDoAluno
        fields = '__all__'
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-select'}), 
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
        }