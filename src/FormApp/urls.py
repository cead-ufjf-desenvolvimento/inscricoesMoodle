from django.urls import path
from FormApp import views

urlpatterns = [
    path('thanks/', views.thanks, name='thanks'),
    path('inscricoes/', views.CadastroAlunoCreateView.as_view(), name='aluno_cadastro'),
    path('cadastro/curso', views.CadastroCursoCreateView.as_view(), name='curso-cadastro'),
]