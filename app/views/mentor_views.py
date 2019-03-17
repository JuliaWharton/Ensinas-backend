from django.shortcuts import render, redirect
from app.models import Estudante, Materia, Mentor, Solicitacao
from app.auth import mentor_auth

def home(request):
	return redirect('app_mentor_solicitacoes')

def solicitacoes(request):
	mentor = mentor_auth.get(request)
	
	if mentor is not None:
		if mentor.aprovado:
			solicitacoes = Solicitacao.objects.filter(mentor=mentor, oculto=False)

			return render(request, 'mentor_solicitacoes.html', {
				'mentor': mentor,
				'solicitacoes': solicitacoes
			})
		else:
			sweetify.error(request, 'Acesso restrito!', text='Seu cadastro ainda não foi aprovado! Por favor aguarde o contato da nossa equipe!', button='Ok', timer=5000)
			return redirect('app_auth_login')
	else:
		sweetify.error(request, 'Acesso restrito!', text='Você precisa estar autenticado para acessar esta página.', button='Ok', timer=5000)
		return redirect('app_auth_login')