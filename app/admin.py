from django.contrib import admin
from app.models import Aluno, Materia, Professor

# Register your models here.
@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ['nome']

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    ordering = ('nome',)
    search_fields = ['nome', 'email']

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'aprovado', 'instituicao', 'curso')
    ordering = ('nome', 'email')
    search_fields = ['nome', 'email', 'instituicao', 'curso']