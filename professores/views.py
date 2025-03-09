#indexa as urls do projeto, define o que deve ser mostrado quando recebe uma requisição

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def professorPage(request):

    token = request.GET.get('token')
    token_salvo = request.session.get('token_protegido')

    if not token or token != token_salvo:
        return redirect("login")

    del request.session['token_protegido']
    return render(request, "professor.html")