from .models import Usuario
from alunos.views import alunoPage
from professores.views import professorPage 

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