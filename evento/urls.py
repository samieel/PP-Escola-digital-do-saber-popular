from django.urls import path
from . import views

urlpatterns = [
    path('', views.exibir_evento, name='exibir_evento'),
]