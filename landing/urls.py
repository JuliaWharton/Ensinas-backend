from django.urls import include, path
from landing.views import landing
from app import views

urlpatterns = [
    path('', landing, name='home'),
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('app_aluno', views.app_aluno, name='app_aluno'),
    path('app_professor', views.app_professor, name='app_professor'),
]
