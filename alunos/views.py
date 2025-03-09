from django.shortcuts import render
from django.shortcuts import redirect
from .models import Aluno

# Create your views here.
def alunoPage(request):

    token = request.GET.get('token')
    token_salvo = request.session.get('token_protegido')

    if not token or token != token_salvo:
        return redirect("login")

    
    aluno_id = request.session.get('id')
    aluno = Aluno.objects.get(id=aluno_id)

    aluno_dados = {
        "nome": aluno.nomeAluno,
        "treino": ""
    }
    del request.session['token_protegido']
    return render(request, "aluno.html", aluno_dados)