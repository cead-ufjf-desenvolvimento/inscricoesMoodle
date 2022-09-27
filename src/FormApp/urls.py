from django.urls import path
from FormApp import views

urlpatterns = [
    path('thanks/', views.thanks, name='thanks'),
    path('thanks2/', views.thanks2, name='thanks2'),
    path('inscricoes/', views.CadastroAlunoCreateView.as_view(), name='aluno_cadastro'),
    # path('cadastro/curso', views.CadastroCursoCreateView.as_view(), name='curso-cadastro'),
]