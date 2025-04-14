#indexa as urls do projeto, define o que deve ser mostrado quando recebe uma requisição

from django.shortcuts import render
from django.shortcuts import redirect
from .models import Professor
from core.dao import *
from .dao import *
from core.views import verifica_se_logado


def professorPage(request):

    if(verifica_se_logado(request) and request.session.get('id_tipo') == 2):
        professor_id = request.session.get('id_professor')
        professor = Professor.objects.get(id=professor_id)
        professor_dados = {
            "nome": professor.nomeProfessor,
            "token": request.session['token_protegido']
        }
        return render(request, "professor.html", professor_dados)
    
    return redirect("login")

def cadastrar_exercicio_page(request):

    info = ""
    erro = ""

    if(verifica_se_logado(request) and request.session.get('id_tipo') == 2):

        if request.method == "POST":
            musculo = request.POST.get("musculo")
            nome_exercicio = request.POST.get("exercicio")

            registrar_exercicio(nome_exercicio, musculo)
            info = "exercicio registrado"

        musculos = {
                "token": request.session['token_protegido'],
                 "musculos": buscar_musculos(),
                 "info": info,
                 "erro": erro
        }

        return render(request, "cadastrar_exercicio.html", musculos)
    
    return redirect("login")

def plano_de_treino_page(request):

    info = ""
    erro = ""
    id_professor = request.session.get('id_professor')

    if(verifica_se_logado(request) and request.session.get('id_tipo') == 2):

        dados = {
            "alunos" : listar_alunos(id_professor),
            "token": request.session['token_protegido'],
        }

        if request.method == "POST":
            
            if(request.path == "/professor/planos/novo_treino"):
                novo_treino(request)
            elif(request.path == "/professor/planos/editar_treino"):
                editar_treino(request)
            elif(request.path == "/professor/planos/deletar_treino"):
                deletar_treino(request)
                
            aluno_id = request.POST.get("aluno")
            dia_da_semana_numero = request.POST.get("dia")
            if( aluno_id.isdigit() and dia_da_semana_numero.isdigit()):

                #mantendo as mesmas opções que o professor selecionou
                dados["aluno"] = aluno_id
                dados["dia_selecionado"] = dia_da_semana_numero

                #procurar treinos de um aluno para aquele dia da semana específico
                treinos = treinos_no_dia(int(dia_da_semana_numero), aluno_id)
                dados["treinos"] = treinos
                dados["exercicios"] = listar_exercicios()

        return render(request, "planos.html", dados)
    
    return redirect("login")

def novo_treino(request):
    aluno = request.POST.get("aluno")
    exercicio = request.POST.get("exercicio")
    series = request.POST.get("series")
    repeticoes = request.POST.get("reps")
    observacoes = request.POST.get("obs")
    dia_da_semana = request.POST.get("dia")
    plano_de_treino = PlanoDeTreino.objects.get(idAluno = aluno).id

    if aluno.isdigit() and exercicio.isdigit() and series.isdigit() and repeticoes.isdigit() and dia_da_semana.isdigit() and plano_de_treino:
        registrar_treino(plano_de_treino, dia_da_semana, exercicio, series,repeticoes, observacoes)

def editar_treino(request):
    if(request.POST.get("save_treino")): 
        treino = request.POST.get("save_treino")
        exercicio = request.POST.get("exercicio")
        series = request.POST.get("series")
        repeticoes = request.POST.get("reps")
        observacoes = request.POST.get("obs")

        if exercicio.isdigit() and series.isdigit() and repeticoes.isdigit() and treino.isdigit():
            mudar_treino(treino,exercicio, series,repeticoes, observacoes)

def deletar_treino(request):
    
    if(request.POST.get("save_treino")): 
        treino = request.POST.get("save_treino")
        if treino.isdigit():
            excluir_treino(treino)



