from django.shortcuts import render
from django.shortcuts import redirect
from .models import Aluno
from .dao import * 
from core.models import *
# Create your views here.
def alunoPage(request):

    # token = request.GET.get('token')
    # token_salvo = request.session.get('token_protegido')

    # if not token or token != token_salvo:
    #     return redirect("login")

    
    aluno_id = request.session.get('id')
    aluno = Aluno.objects.get(id=aluno_id)

    aluno_dados = {
        "nome": aluno.nomeAluno,
        "treinos": formatar_treinos(retornar_treinos_de_um_aluno(aluno))
    }
    # del request.session['token_protegido']

    return render(request, "aluno.html", aluno_dados)

def formatar_treinos(query_geral: list):

    dias = ["Segunda", "Terça", "Quarta",
             "Quinta", "Sexta", "Sábado",
             "Domingo"]
    tabela_geral_de_treinos = {
        "Segunda": [],
        "Terça": [],
        "Quarta": [],
        "Quinta": [],
        "Sexta": [],
        "Sábado": [],
        "Domingo": []
    }
    treinos_de_cada_dia = []

    i = int(0)
    for query_do_dia in query_geral:
            for treino in query_do_dia: 
                treino_lista = [treino.exercicio.nomeExercicio, treino.series,
                                treino.repeticoes, treino.observacoes]
                treinos_de_cada_dia.append(treino_lista)
                tabela_geral_de_treinos[dias[i]] = treinos_de_cada_dia

            i+=1
            treinos_de_cada_dia = []

    print(tabela_geral_de_treinos)
    return tabela_geral_de_treinos
        

    