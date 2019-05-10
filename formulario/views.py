from django.shortcuts import render
from .models import AULA
from . import forms
from .forms import CAtividade
# Create your views here.

def criar_atividade(request):
    if request.method == "POST":
        form = CAtividade(request.POST)

        if form.is_valid():
            form.save()


    form = CAtividade()
    key = AULA.objects.all()
    return render(request, 'formulario/formulario.html', {'form':form}, {'key':key})

    