from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
import sweetify

from app.models import Estudante, Materia, Mentor, Solicitacao
from app.auth import estudante_auth

def home(request):
	estudante = estudante_auth.get(request)
	
	if estudante is not None:
		return redirect('app_estudante_materia', 0)		
	else:
		return redirect('app_auth_login')


def materia(request, id_materia):
	estudante = estudante_auth.get(request)
	print(estudante); 	
	if estudante is not None:
		materias = Materia.objects.all()
		if id_materia is not 0:
			mentores = Mentor.objects.filter(materia=id_materia, aprovado=True)
		else:
			mentores = Mentor.objects.filter(aprovado=True)

		return render(request, 'estudante_materia.html', {
			"materias": materias, 
			"materia_atual": id_materia,
			"mentores": mentores,
			"estudante": estudante
			})
	else:
		sweetify.error(request, 'Acesso restrito!', text='Você precisa estar autenticado para acessar esta página.', button='Ok', timer=3000)
		
		return redirect('app_auth_login')

def contato(request, id_mentor, id_materia):
	estudante = estudante_auth.get(request)

	if estudante is not None:
		try:
			mentor = Mentor.objects.get(pk=id_mentor)

			solicitacao = Solicitacao.objects.filter(mentor=mentor,estudante=estudante).get_or_create(mentor=mentor, estudante=estudante, oculto=False)

			sweetify.success(request, 'Tudo certo!', text='Solicitação de contato enviada para o mentor! Favor aguardar que o mentor entrará em contato.', button='Ok', timer=5000)
		except Mentor.DoesNotExist:
			pass
		return redirect('app_estudante_materia', id_materia)
	else:
		sweetify.error(request, 'Acesso restrito!', text='Você precisa estar autenticado para acessar esta página.', button='Ok', timer=3000)

		return redirect('app_auth_login')
