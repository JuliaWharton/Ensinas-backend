from django.contrib import admin
from app.models import Materia

# Register your models here.
@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ['nome']