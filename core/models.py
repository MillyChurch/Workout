from django.db import models
from professores.models import Professor
from alunos.models import Aluno

# Create your models here.

class PlanoDeTreino(models.Model):
    idAluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    idProfessor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    dataInicio = models.DateField()
    dataFim = models.DateField()

class Musculo(models.Model):
    nomeMusculo = models.CharField(max_length=100, null=False, blank=False)

class Exercicio(models.Model):
    nomeExercicio = models.CharField(max_length=100, null=False, blank=False)
    musculo = models.ForeignKey(Musculo, on_delete=models.CASCADE)

class Treino(models.Model):
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    planoDeTreino = models.ForeignKey(PlanoDeTreino, on_delete=models.CASCADE)
    diaDaSemana = models.IntegerField()
    series = models.IntegerField()
    repeticoes = models.IntegerField()
    observacoes = models.TextField()


