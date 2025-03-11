from core.models import *
from .models import Aluno
from professores.views import professorPage 
from django.shortcuts import redirect

def retornar_treinos_de_um_aluno(aluno: Aluno):

    """
    Retorna um set com os treinos de um aluno durante cada dia da semana
    """
    
    plano_de_treino = PlanoDeTreino.objects.get(idAluno = aluno.id)

    treinos_da_semana = []
    for dia in range(1,8):
        treinos_da_semana.append((Treino.objects.
                                  filter(planoDeTreino = plano_de_treino)
                                  .filter(diaDaSemana = dia)))
        

    return treinos_da_semana
