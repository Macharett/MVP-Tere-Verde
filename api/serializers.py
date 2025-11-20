from rest_framework import serializers
from .models import Parque, Trilha, Evento


class TrilhaSerializer(serializers.ModelSerializer):
    status_aberta_display = serializers.SerializerMethodField()
    dificuldade_display = serializers.CharField(source='get_dificuldade_display')

    class Meta:
        model = Trilha
        fields = (
            'id', 
            'nome', 
            'descricao', 
            'dificuldade',
            'dificuldade_display', 
            'distancia_km', 
            'tempo_estimado_horas', 
            'status_aberta',
            'status_aberta_display', 
        )

    def get_status_aberta_display(self, obj):
        return "Aberta" if obj.status_aberta else "Fechada"



class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = (
            'id', 
            'titulo', 
            'descricao', 
            'data_inicio', 
            'data_fim', 
            'disponibilidade'
        )

class ParqueSerializer(serializers.ModelSerializer):
    trilhas = TrilhaSerializer(many=True, read_only=True)
    eventos = EventoSerializer(many=True, read_only=True)
    
    nome_display = serializers.CharField(source='get_nome_display')

    class Meta:
        model = Parque
        fields = (
            'id', 
            'nome', 
            'nome_display',
            'descricao_geral', 
            'altitude_media', 
            'horario_funcionamento',
            'trilhas',  
            'eventos',
        )