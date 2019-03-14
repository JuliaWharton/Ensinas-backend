from django.shortcuts import render
from app.models import Materia

def auth_cadastro(request):
    return render(request, 'auth_cadastro.html')

def auth_login(request):
    return render(request, 'auth_login.html')

def aluno_home(request):
    materias = Materia.objects.all()

    return render(request, 'aluno_home.html', {
        "materias": materias
        })


def aluno_materia(request, id_materia):
    materias = Materia.objects.all()
    materia_atual = Materia.objects.get(pk=id_materia)

    return render(request, 'aluno_home.html', {
        "materias": materias, 
        "materia_atual": materia_atual
        })

def professor_home(request):
    return render(request, 'professor_home.html')