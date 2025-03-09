from django.db import models
from professores.models import Professor
from alunos.models import Aluno

# Create your models here.
class TiposDeUsuario(models.Model):
    idTipo = models.IntegerField(primary_key=True)
    nomeTipo = models.CharField(max_length=100, null=False, blank=False)

class Usuario(models.Model):
    loginUsuario = models.CharField(max_length=100, null=False, blank=False)
    senhaUsuario = models.CharField(max_length=100, null=False, blank=False)
    idTipo = models.ForeignKey(TiposDeUsuario, on_delete=models.CASCADE)
    idAluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True, blank=True)
    idProfessor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True, blank=True)

