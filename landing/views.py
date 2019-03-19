from django.shortcuts import render
from app.auth import estudante_auth

# Create your views here.
def landing(request):
    estudante = estudante_auth.get(request); 
    contexto = {
        'path': 'app/auth/login'
    } 
    if estudante is not None:
        print('gaaaay')
        contexto['path'] = '/app/estudante/materia/0'
    print(contexto['path'])
    
    return render(request, 'landing.html', contexto)
