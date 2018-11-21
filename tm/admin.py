from django.contrib import admin
from tm.models import Pessoa, Aula

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'observacoes', 'telefone')


class AulaAdmin(admin.ModelAdmin):
    list_display = ('ritmo', 'professor', 'dia_semana', 'hora_inicio', 'duracao')


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Aula, AulaAdmin)