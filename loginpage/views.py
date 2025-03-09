from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse
from django.http import HttpRequest
from alunos.views import alunoPage
from professores.views import professorPage 
from django.shortcuts import redirect
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
    else:
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")
        try:
            usuarioObj = Usuario.objects.get(loginUsuario=usuario)
        except:
            to_request["usuario"] = usuario
            to_request["senha"] = senha
            to_request["erro"] = "Usuário ou Senha incorretos"
            return render(request, "loginpage/tela_de_login.html", to_request)
        
        if(usuarioObj):
            if(usuarioObj.senhaUsuario == senha):
                request.user = usuarioObj.loginUsuario
                token = secrets.token_urlsafe(16)
                request.session['token_protegido'] = token

                if usuarioObj.idAluno:
                    request.session["id"] = usuarioObj.idAluno.id
                    # request.session['idAluno'] = usuarioObj.idAluno
                    return redirect(f'/aluno/?token={token}')
                # request.session['idProfessor'] = usuarioObj.idProfessor
                request.session["id"] = usuarioObj.idAluno.id
                return redirect(f'/professor/?token={token}')
            
        to_request["usuario"] = usuario
        to_request["senha"] = senha
        to_request["erro"] = "Usuário ou Senha incorretos"
        return render(request, "loginpage/tela_de_login.html", to_request)
