from django.shortcuts import render, redirect
from app.models import Contato, Estudante, Materia, Mentor

def home(request):
	return render(request, 'mentor_home.html')