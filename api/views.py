from rest_framework import viewsets
from .models import Parque, Trilha, Evento
from .serializers import ParqueSerializer, TrilhaSerializer, EventoSerializer
from api import models


# RF06: Consulta de Parques (API)
class ParqueViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint de API que permite listar e visualizar detalhes dos Parques.
    """
    queryset = Parque.objects.all()
    serializer_class = ParqueSerializer


# RF07: Consulta de Trilhas (API)
class TrilhaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint de API que permite listar e visualizar detalhes das Trilhas.
    Apenas trilhas abertas são listadas por padrão.
    """
    # Exibe apenas trilhas abertas para o público
    queryset = Trilha.objects.filter(status_aberta=True) 
    serializer_class = TrilhaSerializer
    
    # Permite filtrar trilhas por Parque (ex: /api/trilhas/?parque=1)
    filterset_fields = ['parque', 'dificuldade']


# RF08: Consulta de Eventos (API)
class EventoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint de API que permite listar e visualizar Eventos e Notícias.
    """
    # Filtra para mostrar apenas eventos que ainda não terminaram
    queryset = Evento.objects.filter(data_fim__isnull=True) | Evento.objects.filter(data_fim__gte=models.DateTimeField())
    serializer_class = EventoSerializer
    
    ordering_fields = ['data_inicio'] 
    
    filterset_fields = ['parque']