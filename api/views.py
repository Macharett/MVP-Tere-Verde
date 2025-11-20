from rest_framework import viewsets
from django.db.models import Q
from django.utils import timezone
from .models import Parque, Trilha, Evento
from .serializers import ParqueSerializer, TrilhaSerializer, EventoSerializer


# RF06: Consulta de Parques (API)
class ParqueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Parque.objects.all()
    serializer_class = ParqueSerializer


# RF07: Consulta de Trilhas (API)
class TrilhaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Trilha.objects.filter(status_aberta=True)
    serializer_class = TrilhaSerializer
    filterset_fields = ['parque', 'dificuldade']


# RF08: Consulta de Eventos (API)
class EventoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Evento.objects.filter(
        Q(data_fim__isnull=True) | Q(data_fim__gte=timezone.now())
    )
    serializer_class = EventoSerializer
    ordering_fields = ['data_inicio']
    filterset_fields = ['parque']
