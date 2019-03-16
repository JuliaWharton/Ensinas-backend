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