from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=255,null=True,blank=True)
    data_inicio = models.DateTimeField(null=True,blank=True)
    data_fim = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.nome
