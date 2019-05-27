from django.shortcuts import render, redirect
from .models import AULA
from . import forms
from .forms import CAtividade, CPTexto
# Create your views here.

def criar_atividade(request):
    if request.method == "POST":
        form = CAtividade(request.POST)

        if form.is_valid():
            print("meu deus")
            post = form.save(commit=False)
            n = (AULA.objects.count()+ 1)
            post.number = n
            post.save()
            key = post.codigo
            return redirect('utexto/%s' %key )

            """return render(request, 'formulario/utext.html', {'formt':formt}, {'aula':newaula})
                
            if formt.is_valid():
                formt.save()
                return render(request, 'formulario/formulario.html')"""


    form = CAtividade()     
    return render(request, 'formulario/formulario.html', {'form':form})

def criar_texto(request):

    if request.method == "POST":
        formt = CPTexto(request.POST)

        if formt.is_valid():
            formt.save()
            return redirect('/formulario/sucesso/%s' %key)

    formt = CPTexto()
    return render(request, 'formulario/text.html', {'formt':formt})

def criar_utexto(request, key):
    aul = AULA.objects.get(codigo=key)
    print (key)

    if request.method == "POST":
        formt = CPTexto(request.POST)
        

        if formt.is_valid():
            formt.save()
            return redirect('/formulario/sucesso/%s' %key)

    formt = CPTexto()
    return render(request, 'formulario/utext.html', {'formt':formt, 'aul':key})

def sucesso(request, key):
    return render(request, 'formulario/sucesso.html', {'key':key})