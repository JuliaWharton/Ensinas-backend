from django.shortcuts import render, redirect
from app.models import Estudante, Materia, Mentor

def home(request):
	return redirect('app_mentor_solicitacoes')

def solicitacoes(request):
	return render(request, 'mentor_solicitacoes.html')