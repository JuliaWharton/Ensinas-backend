from django.contrib import admin
from app.models import Aluno, Materia

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