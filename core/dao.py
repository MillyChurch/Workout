from .models import *
from datetime import date
import re


def buscar_musculos():
    return Musculo.objects.all()

def registrar_exercicio(nome_exercicio: str, musculo_id: int):
    nome_exercicio = nome_exercicio.capitalize()
    musculo = Musculo.objects.get(id = musculo_id)
    exercicio = Exercicio(nomeExercicio = nome_exercicio, musculo = musculo)
    exercicio.save()

def treinos_no_dia(dia: int, aluno_id: int):
    aluno = Aluno.objects.get(id = aluno_id)
    treinos =  Treino.objects.filter(planoDeTreino= PlanoDeTreino.objects.get(idAluno = aluno), diaDaSemana= dia)
    return treinos

def listar_exercicios():
    return Exercicio.objects.all()

def registrar_treino(id_plano: int, dia_da_semana: int, exercicio:int, series: int, repeticoes: int, obs: str):
    
    obj_plano = PlanoDeTreino.objects.get(id = id_plano)
    obj_exercicio = Exercicio.objects.get(id = exercicio)

    treino = Treino(
        exercicio = obj_exercicio,
        planoDeTreino= obj_plano,
        diaDaSemana=dia_da_semana,
        series = series,
        observacoes = obs,
        repeticoes=repeticoes
    )
    treino.save()

def mudar_treino(id_treino: int, exercicio:int, series: int, repeticoes: int, obs: str):
    
    if(Treino.objects.filter(id = id_treino)):
        treino = Treino.objects.get(id = id_treino)
        obj_exercicio = Exercicio.objects.get(id = exercicio)
        treino.exercicio = obj_exercicio
        treino.series = series
        treino.repeticoes = repeticoes
        treino.observacoes = obs
        treino.save()

def excluir_treino(id_treino: int):
    if(Treino.objects.filter(id = id_treino)):
        treino = Treino.objects.get(id = id_treino)
        treino.delete()

def registrar_plano(
        id_aluno: int,
        id_professor: int
):
    professor = Professor.objects.get(id = id_professor)
    aluno = Aluno.objects.get(id = id_aluno)
    plano = PlanoDeTreino(idAluno = aluno,
                          idProfessor = professor)
    plano.save()

def listar_profs():
    return Professor.objects.all()

def listar_alunos():
    return Aluno.objects.all()

def retorna_planos():
    return PlanoDeTreino.objects.all()

def vincular_plano_de_treino(aluno_id, professor_id):
    aluno = Aluno.objects.get(id = aluno_id)
    professor = Professor.objects.get(id = professor_id)

    plano = PlanoDeTreino(idProfessor = professor,
                        idAluno = aluno,
                        dataInicio = date.today()
                        )
    plano.save()

def mudar_plano(aluno_id, professor_id):
    aluno = Aluno.objects.get(id = aluno_id)
    plano = PlanoDeTreino.objects.get(idAluno = aluno)
    plano.idProfessor = Professor.objects.get(id=professor_id)
    plano.save()