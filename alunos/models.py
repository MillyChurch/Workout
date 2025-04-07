from django.db import models

# Create your models here.

class Aluno(models.Model):
    nomeAluno = models.CharField(max_length=100, null=False, blank=False)
    cpfAluno = models.CharField(max_length=11, null=False, blank=False)
    


