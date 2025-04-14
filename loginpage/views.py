from django.shortcuts import render
from .models import Usuario
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

        #se adm
        if(usuario_objeto.idTipo == retorna_tipo_usuario(3)):
            request.session["id_tipo"] = 3
            request.user = usuario_objeto.loginUsuario
            token = secrets.token_urlsafe(16)
            request.session['token_protegido'] = token
            return redirect(f'/gerencia/?token={token}')

        #se recepão
        elif(usuario_objeto.idTipo == retorna_tipo_usuario(4)):
            request.session["id_tipo"] = 4
            request.user = usuario_objeto.loginUsuario
            token = secrets.token_urlsafe(16)
            request.session['token_protegido'] = token
            return redirect(f'/gerencia/?token={token}')

        elif usuario_objeto.idTipo == retorna_tipo_usuario(1):
            request.session["id_tipo"] = 1
            request.session["id_aluno"] = usuario_objeto.idAluno.id
            return redirect(f'/aluno/?token={token}')
        
        #se é professor
        request.session["id_tipo"] = 2
        request.session["id_professor"] = usuario_objeto.idProfessor.id
        return redirect(f'/professor/?token={token}')
        
    to_request["usuario"] = usuario
    to_request["senha"] = senha
    to_request["erro"] = "Usuário ou Senha incorretos"
    return render(request, "loginpage/tela_de_login.html", to_request)
