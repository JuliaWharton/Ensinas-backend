from django.urls import include, path
from . import views

urlpatterns = [
    path('auth/cadastro', views.auth_cadastro, name='app_auth_cadastro'),
    path('auth/login', views.auth_login, name='app_auth_login'),
    path('aluno/home', views.aluno_home, name='app_aluno_home'),
    path('professor/home', views.professor_home, name='app_professor_home'),
]