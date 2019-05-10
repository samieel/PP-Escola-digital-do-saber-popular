from django.urls import path
from . import views

urlpatterns = [
    path('', views.criar_atividade, name='criar_atividade'),
]