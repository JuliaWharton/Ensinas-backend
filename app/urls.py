from django.urls import include, path
from . import views

urlpatterns = [
    path('auth/cadastro', views.auth_cadastro, name='app_auth_cadastro'),
    path('auth/login', views.auth_login, name='app_auth_login'), 
    path('auth/logout', views.auth_logout, name='app_auth_logout'),
    path('estudante/home', views.estudante_home, name='app_estudante_home'),
    path('estudante/home/<int:id_materia>', views.estudante_materia, name='app_estudante_materia'),
    path('estudante/contato/<int:id_mentor>/<int:id_materia>/', views.estudante_contato_materia, name='app_estudante_contato'),
    path('estudante/contato/<int:id_mentor>/', views.estudante_contato, name='app_estudante_contato'),
    path('mentor/home', views.mentor_home, name='app_mentor_home'),
]