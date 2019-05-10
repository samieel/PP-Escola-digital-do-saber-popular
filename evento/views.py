from django.shortcuts import render
from .models import EVENTO

# Create your views here.
def exibir_evento(request):
    evento = EVENTO.objects.all()

    return render(request, 'evento/evento.html', {'evento':evento})