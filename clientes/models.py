from django.db import models

# Create your models here.

class Cliente (models.Model):
    nome = models.CharField(max_length=200, null=True, blank=False),
    email = models.EmailField(max_length=75, null=True, blank=False),



