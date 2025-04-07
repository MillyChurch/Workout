from .models import Usuario
from professores.models import Professor
from alunos.models import Aluno
from alunos.views import alunoPage
from professores.views import professorPage 
from .models import TiposDeUsuario

def retorna_usuario_se_existir(usuario_nome: str):
    try:
        return Usuario.objects.get(loginUsuario=usuario_nome)
    except:
        return None
    
def retorna_se_usuario_e_senha_coincidem(senha: str, usuario: Usuario):
    if usuario.senhaUsuario == senha:
        return True
    return False

def retorna_se_aluno(usuario: Usuario):
    if(usuario.idAluno):
         return True
    return False

def novo_login_prof(login: str, senha:str, professor: int):
    
    user = Usuario(loginUsuario = login, senhaUsuario = senha, idTipo = TiposDeUsuario.objects.get(idTipo = 2),
                   idProfessor = Professor.objects.get(id = professor))
    user.save()
    return user

def novo_login_aluno(login: str, senha:str, aluno: int):
    user = Usuario(loginUsuario = login, senhaUsuario = senha, idTipo = TiposDeUsuario.objects.get(idTipo = 1),
                   idAluno = Aluno.objects.get(id = aluno))
    user.save()
    return user

def retorna_tipo_usuario(tipo: int):
    return TiposDeUsuario.objects.get(idTipo = tipo)

def listar_professores():
    return Professor.objects.all()

def verificar_se_login_existe(login:str):
    return Usuario.objects.filter(loginUsuario=login).exists()