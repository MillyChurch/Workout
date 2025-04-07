from alunos.models import Aluno
from .models import Professor 
from core.models import *

def gerar_treino(exercicio: Exercicio, series: int,
                 dia_da_semana: int, repeticoes: int,
                 plano_de_treino_id: int, obs: str):
    treino = Treino(exercicio_id= exercicio, series= series,
                    dia_da_semana = dia_da_semana, repeticoes=repeticoes,
                    observacoes = obs
                    )
    treino.save()

def cadastrar_plano_de_treino(aluno: Aluno, professor:Professor, data_inicio, data_fim):
    plano = PlanoDeTreino(idAluno=aluno, data_fim = data_fim,
                          idProfessor=professor,
                          data_inicio = data_inicio)
    plano.save()

def listar_alunos(professor_id:str):
    professor = Professor.objects.get(id = professor_id)
    planos = PlanoDeTreino.objects.filter(idProfessor = professor)
    alunos = Aluno.objects.filter(id__in=planos.values_list('idAluno',
                                                            flat=True))
    return alunos

def novo_prof(nome: str, cpf:str):
    prof = Professor(nomeProfessor = nome, cpfProfessor = cpf)
    prof.save()
    return prof.id

def verifica_se_existe_professor_com_o_cpf(cpf: str):
    return Professor.objects.filter(cpfProfessor=cpf).exists()

def deletar_prof(id: int):
    prof = Professor.objects.get(id=id)
    prof.delete()