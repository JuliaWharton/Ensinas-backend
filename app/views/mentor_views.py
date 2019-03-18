from django.shortcuts import render, redirect
import sweetify

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
			sweetify.error(request, 'Acesso restrito!', html='<p>Seu cadastro ainda não foi aprovado!</p><p>Por favor aguarde o contato da nossa equipe!</p>', persistent=True)
			return redirect('app_auth_login')
	else:
		sweetify.error(request, 'Acesso restrito!', text='Você precisa estar autenticado para acessar esta página.', button='Ok', timer=3000)
		return redirect('app_auth_login')

def contato(request, id_solicitacao):
	mentor = mentor_auth.get(request)
	
	if mentor is not None:
		if mentor.aprovado:
			try:
				solicitacao = Solicitacao.objects.get(pk=id_solicitacao)
				
				sweetify.info(request, 'Entrar em contato!', html=f'<p>Para entrar em contato com {solicitacao.estudante.nome}, envie um e-mail.</p><p><a href="mailto:{solicitacao.estudante.email}">Enviar E-mail</a></p>', persistent=True)
			except Solicitacao.DoesNotExist:
				sweetify.error(request, 'Erro!', text='Solicitação não foi encontrada!')
			return redirect('app_mentor_solicitacoes')
		else:
			sweetify.error(request, 'Acesso restrito!', html='<p>Seu cadastro ainda não foi aprovado!</p><p>Por favor aguarde o contato da nossa equipe!</p>', persistent=True)
			return redirect('app_auth_login')
	else:
		sweetify.error(request, 'Acesso restrito!', text='Você precisa estar autenticado para acessar esta página.', button='Ok', timer=3000)
		return redirect('app_auth_login')

def ocultar(request, id_solicitacao):
	mentor = mentor_auth.get(request)
	
	if mentor is not None:
		if mentor.aprovado:
			try:
				solicitacao = Solicitacao.objects.get(pk=id_solicitacao)
				solicitacao.oculto = True
				solicitacao.save()

				sweetify.info(request, 'Solicitação removida!', text=f'A solicitação de {solicitacao.estudante.nome} não aparecerá mais para você.')
			except Solicitacao.DoesNotExist:
				sweetify.error(request, 'Erro!', text='Solicitação não foi encontrada!')
			return redirect('app_mentor_solicitacoes')
		else:
			sweetify.error(request, 'Acesso restrito!', html='<p>Seu cadastro ainda não foi aprovado!</p><p>Por favor aguarde o contato da nossa equipe!</p>', persistent=True)
			return redirect('app_auth_login')
	else:
		sweetify.error(request, 'Acesso restrito!', text='Você precisa estar autenticado para acessar esta página.', button='Ok', timer=3000)
		return redirect('app_auth_login')
