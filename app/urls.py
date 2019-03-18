from django.urls import include, path
from app.views import auth_views, estudante_views, mentor_views

urlpatterns = [
    path('auth/cadastro', auth_views.cadastro, name='app_auth_cadastro'),
    path('auth/login', auth_views.login, name='app_auth_login'), 
    path('auth/logout', auth_views.logout, name='app_auth_logout'),
    path('estudante/home', estudante_views.home, name='app_estudante_home'),
    path('estudante/materia/<int:id_materia>', estudante_views.materia, name='app_estudante_materia'),
    path('estudante/contato/<int:id_mentor>/<int:id_materia>/', estudante_views.contato, name='app_estudante_contato'),
    path('mentor/home', mentor_views.home, name='app_mentor_home'),
    path('mentor/solicitacoes', mentor_views.solicitacoes, name='app_mentor_solicitacoes'),
    path('mentor/solicitacoes/<int:id_solicitacao>/contato', mentor_views.contato, name='app_mentor_contato'),
    path('mentor/solicitacoes/<int:id_solicitacao>/ocultar', mentor_views.ocultar, name='app_mentor_ocultar')
]