from django.shortcuts import render
from formulario.models import AULA, TEXTO_AULA
# Create your views here.
def exibir_aula(request):
    aula = AULA.objects.all()
    return render(request, 'aula/aulas.html', {'aula':aula})

def aula_completa(request, number):
    aula = AULA.objects.get(number=number)
    textos = TEXTO_AULA.objects.filter(codigo_aula=aula.codigo)
    return render(request, 'aula/aula_completa.html', {'aula':aula, 'textos':textos})