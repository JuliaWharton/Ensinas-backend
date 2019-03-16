from django import forms
from app.models import Estudante, Mentor

class EstudanteLoginForm(forms.ModelForm):
    prefix = "login-estudante"

    class Meta:
        model = Estudante
        fields = [
            'email',
            'senha'
        ]
        widgets = {
            'senha': forms.PasswordInput
        }

class MentorLoginForm(forms.ModelForm):
    prefix = "login-mentor"

    class Meta:
        model = Mentor
        fields = [
            'email',
            'senha'
        ]
        widgets = {
            'senha': forms.PasswordInput
        }

class EstudanteCadastroForm(forms.ModelForm):
    prefix = "cadastro-estudante"
    senha_confirma = forms.CharField(label="Confirme a Senha", widget=forms.PasswordInput)

    class Meta:
        model = Estudante
        fields = [
            'nome',
            'email',
            'senha',
        ]
        widgets = {
            'senha': forms.PasswordInput
        }

class MentorCadastroForm(forms.ModelForm):
    prefix = "cadastro-mentor"
    senha_confirma = forms.CharField(label="Confirme a Senha", widget=forms.PasswordInput)

    class Meta:
        model = Mentor
        fields = [
            'nome',
            'email',
            'senha',
        ]
        widgets = {
            'senha': forms.PasswordInput
        }