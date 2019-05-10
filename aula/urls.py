from django.urls import path
from . import views

urlpatterns = [
    path('', views.exibir_aula, name='exibir_aula'),
]