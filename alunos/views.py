from django.shortcuts import render
from django.shortcuts import redirect
from .models import Aluno
from .dao import * 
from core.models import *
from core.dao import *

def alunoPage(request):

    token = request.GET.get('token')
    token_salvo = request.session.get('token_protegido')

    if not token or token != token_salvo:
         return redirect("login")

    
    aluno_id = request.session.get('id')
    aluno = Aluno.objects.get(id=aluno_id)
    dia = request.POST.get("dia")
    aluno_dados = {
        "token" : token_salvo,
        "nome": aluno.nomeAluno,
        "treinos": treinos_no_dia(aluno_id=aluno_id, dia=dia),
        "dia_selecionado" : dia
    }

    return render(request, "aluno.html", aluno_dados)



    