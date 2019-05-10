from django.shortcuts import render
from formulario.models import AULA
# Create your views here.
def exibir_aula(request):
    aula = AULA.objects.all()
    return render(request, 'aula/aulas.html', {'aula':aula})