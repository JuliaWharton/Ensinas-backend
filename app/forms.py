from django import forms
from app.models import Estudante, Mentor

class EstudanteLoginForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = [
            'email',
            'senha'
        ]

class MentorLoginForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = [
            'email',
            'senha'
        ]

class EstudanteCadastroForm(forms.ModelForm):
    senha_confirma = forms.CharField(label="Confirme a Senha", widget=forms.PasswordInput)
    class Meta:
        model = Estudante
        fields = [
            'nome',
            'email',
            'senha',
        ]

class MentorCadastroForm(forms.ModelForm):
    senha_confirma = forms.CharField(label="Confirme a Senha", widget=forms.PasswordInput)
    class Meta:
        model = Mentor
        fields = [
            'nome',
            'email',
            'senha',
        ]