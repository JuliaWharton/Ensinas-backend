from django.contrib import admin
from app.models import Estudante, Materia, Mentor, Solicitacao

admin.site.site_title = "Admin Ensinas"
admin.site.site_header = "Administração Ensinas"
admin.site.index_title = "Administração do Sistema"

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)

@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    ordering = ('nome',)
    search_fields = ('nome', 'email')

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'aprovado', 'instituicao', 'curso')
    ordering = ('nome', 'email')
    search_fields = ('nome', 'email', 'instituicao', 'curso')

@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('estudante', 'mentor', 'oculto')
    ordering = ('estudante', 'mentor')
    search_fields = ('estudante', 'mentor')