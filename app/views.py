from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def app_aluno(request):
    return render(request, 'app_aluno.html')

def app_professor(request):
    return render(request, 'app_professor.html')