from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from app.models import Estudante, Mentor
from app.auth import estudante_auth, mentor_auth
from app import forms

def cadastro(request):
    form_estudante = forms.EstudanteCadastroForm()
    form_mentor = forms.MentorCadastroForm()

    return render(request, 'auth_cadastro.html', {
            'form_estudante': form_estudante,
            'form_mentor': form_mentor
    })

def login(request):
	if request.POST.get("do", '') == "login_estudante":
		form_estudante = forms.EstudanteLoginForm(request.POST)

		if form_estudante.is_valid():
			email = form_estudante.cleaned_data["email"]
			senha = form_estudante.cleaned_data["senha"]

			if estudante_auth.login(request, email, senha):
				return redirect("app_estudante_home")
			else:
				form_estudante.add_error("email", "E-mail e/ou senha inválidos.")
	else:
		form_estudante = forms.EstudanteLoginForm()
					
	if request.POST.get("do", '') == "login_mentor":
		form_mentor = forms.MentorLoginForm(request.POST)

		if form_mentor.is_valid():
			return None
	else:
		form_mentor = forms.MentorLoginForm()

	return render(request, 'auth_login.html', {
			'form_estudante': form_estudante,
			'form_mentor': form_mentor
	})

def logout(request):
	estudante_auth.logout(request)

	return redirect('app_auth_login')