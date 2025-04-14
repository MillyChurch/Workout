from django.shortcuts import render
from django.shortcuts import redirect
from .dao import *
from professores.dao import novo_prof
from professores.dao import deletar_prof
from loginpage.dao import *
from professores.dao import verifica_se_existe_professor_com_o_cpf
from alunos.dao import *

def admin_screen(request):

    #Verificar se o usuário tem permissão de estar na tela de gerenciamento
    sessoes_aceitas = [3,4]
    tipo = request.session.get('id_tipo')
    
    if not verifica_se_logado(request) or tipo not in sessoes_aceitas:
            return redirect("login")
    
    dados = {
            "token": request.session['token_protegido'],
            "tipo_user": tipo
        }
    
    #Caso o usuário tenha requisitado um serviço
    if request.method == "POST":

        #cadastrar um professor
        if(request.path == "/adminx/novoProfessor" and tipo == 3):
            return novo_professor(request, dados)
        
        #Deletar um professor
        elif(request.path == "/adminx/deletarProfessor" and tipo == 3):
            del_professor(request)
            redirect("admin_profs")

        #Cadastrar um aluno
        elif(request.path == "/gerencia/novoAluno"):
            return novo_aluno(request, dados)

        #Deletar um aluno
        elif(request.path == "/gerencia/deletarAluno"):
            del_aluno(request)
            redirect("gerencia_alunos")

        #Editar plano de treino de um aluno
        elif(request.path == "/gerencia/editarPlano"):
            editar_plano(request)
            redirect("gerencia_alunos")

        return render(request, "core/gerencia.html", dados)

    #Entrar na tela de cadastrar um professor
    if(request.path == "/adminx/novoProfessor" and tipo == 3):
        return render(request, "core/admin/cadastrar_professor.html", dados)
    
    #Entrar na tela de cadastrar um aluno
    elif(request.path == "/gerencia/novoAluno"):
        dados["professores"] = listar_professores()
        return render(request, "core/cadastrar_aluno.html", dados)

    return render(request, "core/gerencia.html", dados)


#Tela de professores (listagem + cadastrar)
def profs(request):
    tipo = request.session.get('id_tipo')
    
    if not verifica_se_logado(request) or tipo is not 3:
            return redirect("login")
    
    dados = {"token": request.session['token_protegido'], "professores": listar_profs()}
    return render(request, "core/admin/profs.html", dados)

#Tela de alunos (listagem + cadastrar)
def alunos(request):
    sessoes_aceitas = [3,4]
    tipo = request.session.get('id_tipo')
    
    if not verifica_se_logado(request) or tipo not in sessoes_aceitas:
            return redirect("login")
    
    dados = {"token": request.session['token_protegido'],
             "alunos":listar_alunos(),
             "planos" : retorna_planos(),
             "professores": listar_professores()}
    return render(request, "core/alunos.html", dados)

def novo_aluno(request, dados):
    nome = request.POST.get("nomeAluno")
    cpf = request.POST.get("cpfAluno")
    professor = request.POST.get("profResp")
    login = request.POST.get("loginAluno")
    senha = request.POST.get("senhaAluno")

    error = False
    login_erro = ""
    nome_erro = ""
    senha_erro = ""
    cpf_erro = ""


    if(not nome):
        nome_erro = "Nome não pode ser vazio"
        error = True
    if(not cpf):
        cpf_erro = "Cpf não pode ser vazio"
        error = True
    elif verifica_se_existe_aluno_com_o_cpf(cpf):
        cpf_erro = "Cpf de aluno já cadastrado"
        error = True
    elif (not cpf_validacao(cpf)):
        cpf_erro = "Cpf inválido"
        error = True
    if(not senha):
        senha_erro = "Senha não pode ser vazio"
        error = True
    if(not login):
        login_erro = "Login não pode ser vazio"
        error = True
    elif verificar_se_login_existe(login):
        login_erro = "Login já existe"
        error = True

    dados['login_erro'] = login_erro
    dados['senha_erro'] = senha_erro
    dados['cpf_erro'] = cpf_erro
    dados['nome_erro'] = nome_erro
    dados['login'] = login
    dados['senha'] = senha
    dados['cpf'] = cpf
    dados['nome'] = nome
    dados["professores"] = listar_professores()

    if(error):
        return render(request, "core/cadastrar_aluno.html", dados)
    
    id_aluno = novoAluno(nome, cpf)
    novo_login_aluno(login, senha, id_aluno)
    vincular_plano_de_treino(int(id_aluno), int(professor))
    
    return redirect("gerencia_alunos")

def cpf_validacao(cpf:str):
    cpf_numeros = re.sub("[^0-9]", "", cpf)
    if(len(cpf_numeros) != 11):
        return False
    
    soma = sum(int(cpf_numeros[i]) * (10 - i) for i in range(9))
    primeiro_digito = (soma * 10 % 11) % 10

    soma = sum(int(cpf_numeros[i]) * (11 - i) for i in range(10))
    segundo_digito = (soma * 10 % 11) % 10

    return cpf_numeros[-2:] == f"{primeiro_digito}{segundo_digito}"

def novo_professor(request, dados):
    nome = request.POST.get("nomeProfessor")
    cpf = request.POST.get("cpfProfessor")
    login = request.POST.get("loginProfessor")
    senha = request.POST.get("senhaProfessor")

    error = False
    login_erro = ""
    nome_erro = ""
    senha_erro = ""
    cpf_erro = ""


    if(not nome):
        nome_erro = "Nome não pode ser vazio"
        error = True
    if(not cpf):
        cpf_erro = "Cpf não pode ser vazio"
        error = True
    elif (not cpf_validacao(cpf)):
        cpf_erro = "Cpf inválido"
        error = True
    elif verifica_se_existe_professor_com_o_cpf(cpf):
        cpf_erro = "Cpf de professor já cadastrado"
        error = True
    if(not senha):
        senha_erro = "senha não pode ser vazio"
        error = True
    if(not login):
        login_erro = "login não pode ser vazio"
        error = True
    elif verificar_se_login_existe(login):
        login_erro = "login já existe"
        error = True

    dados['login_erro'] = login_erro
    dados['senha_erro'] = senha_erro
    dados['cpf_erro'] = cpf_erro
    dados['nome_erro'] = nome_erro
    dados['login'] = login
    dados['senha'] = senha
    dados['cpf'] = cpf
    dados['nome'] = nome

    if(error):
        return render(request, "core/admin/cadastrar_professor.html", dados)
    
    id_prof = novo_prof(nome, cpf)
    login_prof = novo_login_prof(login, senha, id_prof)
    
    return redirect("admin_profs")

def del_professor(request):
    id = request.POST.get("profs")
    deletar_prof(int(id))

def del_aluno(request):
    id = request.POST.get("aluno")
    deletar_aluno(int(id))

def verifica_se_logado(request):
    token = request.GET.get('token')
    token_salvo = request.session.get('token_protegido')
    
    if not token or token != token_salvo:
        return False

    return True

def editar_plano(request):
    aluno = int(request.POST.get("aluno_id"))
    professor = int(request.POST.get("prof"))
    mudar_plano(aluno, professor)
    return redirect("gerencia_alunos")
