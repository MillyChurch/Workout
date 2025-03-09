"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import loginpage.views 
import alunos.views
import professores.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", loginpage.views.login_screen, name="login"),
    path("aluno/", alunos.views.alunoPage, name="aluno_page"),
    path("professor/", professores.views.professorPage, name="professor_page"),
    # path("pagina_aluno", loginpage.views.login_screen, name="login"),
    # path("pagina_professor", loginpage.views.login_screen, name="login"),
]
