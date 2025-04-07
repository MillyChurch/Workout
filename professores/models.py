# Se comunica com o banco de dados

from django.db import models

# Create your models here.
class Professor(models.Model):
    nomeProfessor = models.CharField(max_length=100, null=False, blank=False)
    cpfProfessor = models.CharField(max_length=11, null=False, blank=False)
