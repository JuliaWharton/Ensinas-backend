from django import forms
from app.models import Estudante, Mentor

class EstudanteLoginForm(forms.Form):
    prefix = "login-estudante"

    email = forms.EmailField(label="E-mail")
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput)

class MentorLoginForm(forms.Form):
    prefix = "login-mentor"

    email = forms.EmailField(label="E-mail")
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput)

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