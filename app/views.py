from django.shortcuts import render

def auth_cadastro(request):
    return render(request, 'auth_cadastro.html')

def auth_login(request):
    return render(request, 'auth_login.html')

def aluno_home(request):
    return render(request, 'aluno_home.html')

def professor_home(request):
    return render(request, 'professor_home.html')