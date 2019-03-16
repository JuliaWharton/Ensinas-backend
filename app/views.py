from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from app.models import Contato, Estudante, Materia, Mentor
from app import forms, auth

def auth_cadastro(request):
    form_estudante = forms.EstudanteCadastroForm()
    form_mentor = forms.MentorCadastroForm()

    return render(request, 'auth_cadastro.html', {
            'form_estudante': form_estudante,
            'form_mentor': form_mentor
    })

def auth_login(request):
	if request.POST.get("do", '') == "login_estudante":
		form_estudante = forms.EstudanteLoginForm(request.POST)

		if form_estudante.is_valid():
			email = form_estudante.cleaned_data["email"]
			senha = form_estudante.cleaned_data["senha"]

			if auth.estudante_login(request, email, senha):
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

def auth_logout(request):
	auth.logout(request)

	return redirect('app_auth_login')

def estudante_home(request):
	estudante = auth.estudante_get(request)
	
	if estudante is not None:
		materias = Materia.objects.all()
		mentores = Mentor.objects.filter(aprovado=True)

		return render(request, 'estudante_home.html', {
			"materias": materias,
			"mentores": mentores,
			"estudante": estudante
			})
	else:
		return redirect('app_auth_login')


def estudante_materia(request, id_materia):
	estudante = auth.estudante_get(request)
	
	if estudante is not None:
		materias = Materia.objects.all()
		materia_atual = Materia.objects.get(pk=id_materia)
		mentores = Mentor.objects.filter(materia=id_materia,aprovado=True)

		return render(request, 'estudante_home.html', {
			"materias": materias, 
			"materia_atual": materia_atual,
			"mentores": mentores,
			"estudante": estudante
			})
	else:
		return redirect('app_auth_login')

def estudante_contato(request, id_mentor):
	estudante = auth.estudante_get(request)

	if estudante is not None:
		try:
			mentor = Mentor.objects.get(pk=id_mentor)

			try:
				contato = Contato.objects.get(mentor=mentor,estudante=estudante)

			except Contato.DoesNotExist:
				contato = Contato()
				contato.mentor = mentor
				contato.estudante = estudante
				contato.save()

		except Mentor.DoesNotExist:
			pass

	return redirect('app_estudante_home')

def estudante_contato_materia(request, id_mentor, id_materia):
	estudante = auth.estudante_get(request)

	if estudante is not None:
		try:
			mentor = Mentor.objects.get(pk=id_mentor)

			try:
				contato = Contato.objects.get(mentor=mentor,estudante=estudante)

			except Contato.DoesNotExist:
				contato = Contato()
				contato.mentor = mentor
				contato.estudante = estudante
				contato.save()

		except Mentor.DoesNotExist:
			pass

	return redirect('app_estudante_materia', id_materia)
	

def mentor_home(request):
	return render(request, 'mentor_home.html')