from rest_framework.viewsets import GenericViewSet , ReadOnlyModelViewSet 
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from gerenciamento.models import Especialidades, Medicos, Horarios, Agenda
from .serializers import EspecialidadesSerializer, MedicosSerializer, AgendaSerializer
from django_filters.rest_framework import DjangoFilterBackend

class EspecialidadesViewSet(ReadOnlyModelViewSet):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['nome']

class MedicosViewSet(ReadOnlyModelViewSet):
    queryset = Medicos.objects.all()
    serializer_class = MedicosSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend,)
    search_fields = ['nome']
    filterset_fields = ['especialidade']

class AgendaViewSet(GenericViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    # def list(self, request):
    #     queryset = Agenda.objects.all()
    #     serializer = AgendaSerializer(queryset, many=True)
    #     return Response(serializer.data)