import uuid
from datetime import datetime   
from django.db import models

# Create your models here.

class AULA(models.Model):
    codigo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome_autor = models.CharField(max_length=50)
    email_autor = models.EmailField(max_length=100, null=True, blank=True)
    titulo_aula = models.CharField(max_length=50)
    descricao_aula = models.TextField(blank=True)
    data = models.DateTimeField(default=datetime.now(), blank=True)

    def Meta():
        ordening ['-data']