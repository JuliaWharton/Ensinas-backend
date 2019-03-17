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

    def clean_senha_confirma(self):
        senha = self.cleaned_data["senha"]
        senha_confirma = self.cleaned_data["senha_confirma"]
        
        if senha != senha_confirma:
            raise forms.ValidationError("As senhas não coicidem.")

        return senha

class MentorCadastroForm(forms.ModelForm):
    prefix = "cadastro-mentor"
    senha_confirma = forms.CharField(label="Confirme a Senha", widget=forms.PasswordInput)

    class Meta:
        model = Mentor
        fields = [
            'nome',
            'materia',
            'email',
            'senha',
        ]
        widgets = {
            'senha': forms.PasswordInput
        }
    
    def clean_senha_confirma(self):
        senha = self.cleaned_data["senha"]
        senha_confirma = self.cleaned_data["senha_confirma"]
        
        if senha != senha_confirma:
            raise forms.ValidationError("As senhas não coicidem.")

        return senha