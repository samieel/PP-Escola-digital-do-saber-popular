from django.urls import path
from . import views

urlpatterns = [
    path('aula', views.criar_atividade, name='criar_atividade'),
    path('texto', views.criar_texto, name='criar_texto'),
    path('utexto/<str:key>/', views.criar_utexto, name='criar_utexto'),
    path('sucesso/', views.sucesso, name='sucesso'),
]