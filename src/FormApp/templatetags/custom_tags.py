from django.template import Library
from django.template.defaultfilters import stringfilter
from FormApp.models import Curso

register = Library()

@register.filter
@stringfilter
def flag_documentos(nome_curso):
    return Curso.objects.get(nome=nome_curso).anexar_documentacao