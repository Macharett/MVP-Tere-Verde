from django.contrib import admin
from .models import Parque, Trilha, Evento

@admin.register(Parque)
class ParqueAdmin(admin.ModelAdmin):
    list_display = ('nome', 'altitude_media', 'horario_funcionamento')
    search_fields = ('nome',)

@admin.register(Trilha)
class TrilhaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'parque', 'dificuldade', 'distancia_km', 'status_aberta')
    list_filter = ('parque', 'dificuldade', 'status_aberta')
    search_fields = ('nome', 'descricao')

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'parque', 'data_inicio', 'disponibilidade')
    list_filter = ('parque', 'data_inicio')
    date_hierarchy = 'data_inicio'
    search_fields = ('titulo', 'descricao')