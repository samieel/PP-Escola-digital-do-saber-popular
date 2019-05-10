from django.db import models

# Create your models here.
class EVENTO (models.Model):
    nome_evento = models.CharField(max_length=50)
    descricao_evento = models.TextField()
    dia_evento = models.DateField()
    hora_evento = models.CharField(max_length=16)
    local_evento = models.CharField(max_length=100)
    link_evento = models.CharField(default='Sem link :(', max_length=200, blank=True)

    def Meta():
        ordering = ['-dia_evento']