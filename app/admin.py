from django.contrib import admin
from app.models import Aluno, Contato, Materia, Professor

admin.site.site_title = "Admin Ensinas"
admin.site.site_header = "Administração Ensinas"
admin.site.index_title = "Administração do Sistema"

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    ordering = ('nome',)
    search_fields = ('nome', 'email')

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'aprovado', 'instituicao', 'curso')
    ordering = ('nome', 'email')
    search_fields = ('nome', 'email', 'instituicao', 'curso')

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'professor', 'oculto')
    ordering = ('aluno', 'professor')
    search_fields = ('aluno', 'professor')