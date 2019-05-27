import uuid
from datetime import datetime   
from django.db import models

# Create your models here.

class AULA(models.Model):
    codigo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField(default=0)
    nome_autor = models.CharField(max_length=50)
    email_autor = models.EmailField(max_length=100, null=True, blank=True)
    titulo_aula = models.CharField(max_length=50, unique=True)
    descricao_aula = models.TextField(blank=True)

    class Meta:
        ordering = ['-number']

class TEXTO_AULA(models.Model):
    codigo_aula = models.CharField(max_length=100, blank=True)
    topico = models.CharField(max_length=50)
    texto = models.TextField()
    
    class Meta:
        ordering = ['-id']

    