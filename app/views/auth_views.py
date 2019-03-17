from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from app.models import Estudante, Mentor
from app.auth import estudante_auth, mentor_auth
from app import forms
import sweetify

def cadastro(request):
	if request.POST.get('do', '') == 'cadastro_estudante':
		form_estudante = forms.EstudanteCadastroForm(request.POST)

		if form_estudante.is_valid():
			form_estudante.instance.senha = make_password(form_estudante.cleaned_data['senha'])
			estudante = form_estudante.save()
			estudante_auth.init_session(request, estudante)		

			sweetify.success(request, 'Cadastro concluido!', text='Seu cadastro foi concluido! Agora basta procurar e encontrar um mentor ideal para você. Caso deseje entrar em contato com algum, basta clicar no botão e iremos solicitar o contato!', button='Ok')

			return redirect('app_estudante_home')	
	else:
		form_estudante = forms.EstudanteCadastroForm()

	if request.POST.get('do', '') == 'cadastro_mentor':
		form_mentor = forms.MentorCadastroForm(request.POST)

		if form_mentor.is_valid():
			form_mentor.instance.senha = make_password(form_mentor.cleaned_data['senha'])
			form_mentor.instance.curso = ""
			form_mentor.instance.instituicao = ""
			mentor = form_mentor.save()
			mentor_auth.init_session(request, mentor)		

			sweetify.success(request, 'Cadastro concluido!', text='Seu cadastro foi concluido! Agora basta aguardar que nossa equipe irá entrar em contato para analisar e aprovar seu cadastro!', button='Ok')

			return redirect('app_auth_login')	
	else:
		form_mentor = forms.MentorCadastroForm()

	return render(request, 'auth_cadastro.html', {
			'form_estudante': form_estudante,
			'form_mentor': form_mentor
	})

def login(request):
	if request.POST.get("do", '') == "login_estudante":
		if estudante_auth.get(request) is None:
			form_estudante = forms.EstudanteLoginForm(request.POST)

			if form_estudante.is_valid():
				email = form_estudante.cleaned_data["email"]
				senha = form_estudante.cleaned_data["senha"]

				if estudante_auth.login(request, email, senha):
					return redirect("app_estudante_home")
				else:
					form_estudante.add_error("email", "E-mail e/ou senha inválidos.")
		else:
			return redirect('app_estudante_home')
	else:
		form_estudante = forms.EstudanteLoginForm()
					
	if request.POST.get('do', '') == 'login_mentor':
		if mentor_auth.get(request) is None:
			form_mentor = forms.MentorLoginForm(request.POST)

			if form_mentor.is_valid():
				email = form_mentor.cleaned_data['email']
				senha = form_mentor.cleaned_data['senha']

				if mentor_auth.login(request, email, senha):
					return redirect('app_mentor_home')
				else:
					form_mentor.add_error('email', 'E-mail e/ou senha inválidos.')
		else:
			return redirect('app_mentor_home')
	else:
		form_mentor = forms.MentorLoginForm()

	return render(request, 'auth_login.html', {
			'form_estudante': form_estudante,
			'form_mentor': form_mentor
	})

def logout(request):
	estudante_auth.logout(request)
	mentor_auth.logout(request)

	return redirect('app_auth_login')