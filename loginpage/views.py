from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse
from django.http import HttpRequest
from alunos.views import alunoPage
from professores.views import professorPage 
from django.shortcuts import redirect
from .dao import *
import secrets

def login_screen(request):
    users = Usuario.objects.all()

    to_request = {
        "users" : users,
        "erro" : "",
        "usuario": "",
        "senha": "",
    }

    if request.method == "GET":
        return render(request, "loginpage/tela_de_login.html")
    
    usuario = request.POST.get("usuario")
    senha = request.POST.get("senha")

    usuario_objeto = retorna_usuario_se_existir(usuario_nome=usuario)
    if not usuario_objeto:
        to_request["usuario"] = usuario
        to_request["senha"] = senha
        to_request["erro"] = "Usuário ou Senha incorretos"
        return render(request, "loginpage/tela_de_login.html", to_request)
    
    if(retorna_se_usuario_e_senha_coincidem(senha, usuario_objeto)):
        request.user = usuario_objeto.loginUsuario
        token = secrets.token_urlsafe(16)
        request.session['token_protegido'] = token

        if retorna_se_aluno(usuario_objeto):
            request.session["id"] = usuario_objeto.idAluno.id
            return redirect(f'/aluno/?token={token}')
        
        #se é professor
        request.session["id"] = usuario_objeto.idProfessor.id
        return redirect(f'/professor/?token={token}')
        
    to_request["usuario"] = usuario
    to_request["senha"] = senha
    to_request["erro"] = "Usuário ou Senha incorretos"
    return render(request, "loginpage/tela_de_login.html", to_request)
