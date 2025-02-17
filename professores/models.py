# Se comunica com o banco de dados

from django.db import models

# Create your models here.
class Professor(models.Model):
    nomeProfessor = models.CharField(max_length=100, null=False, blank=False)