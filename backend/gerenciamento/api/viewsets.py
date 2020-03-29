# standard library
from datetime import date, datetime

# Django, django-rest, django-filters
from django.shortcuts import get_object_or_404
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

# models
from gerenciamento.models import (Agenda, Consultas, Especialidades, Horarios,
                                  Medicos)
# permissions
from gerenciamento.permissions import IsOwner

#serializers
from .serializers import (AgendaSerializer, ConsultasSerializer,
                          EspecialidadesSerializer, MedicosSerializer)


class EspecialidadesViewSet(ReadOnlyModelViewSet):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['nome']


class MedicosViewSet(ReadOnlyModelViewSet):
    queryset = Medicos.objects.all()
    serializer_class = MedicosSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    search_fields = ['nome']
    filterset_fields = ['especialidade']


class AgendaFilter(FilterSet):
    data_inicio = filters.DateFilter(field_name='dia', lookup_expr='gte')
    data_final = filters.DateFilter(field_name='dia', lookup_expr='lte')
    especialidade = filters.CharFilter(field_name='medico__especialidade')

    class Meta:
        model = Agenda
        fields = ['dia', 'medico']


class AgendaViewSet(ReadOnlyModelViewSet):
    queryset = Agenda.objects.exclude(dia__lt=date.today()).order_by('dia')
    serializer_class = AgendaSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = AgendaFilter


class ConsultasViewSet(GenericViewSet):
    queryset = Consultas.objects.all()
    serializer_class = ConsultasSerializer
    permission_classes = [IsOwner, ]

    def list(self, request):
        queryset = Consultas.objects.exclude(agenda__dia__lt=date.today()).order_by('agenda__dia', 'horario__hora').filter(usuario=request.user)
        serializer = ConsultasSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Consultas.objects.all().filter(usuario=request.user)
        consulta = get_object_or_404(queryset, pk=pk)
        serializer = ConsultasSerializer(consulta)

        return Response(serializer.data)

    def create(self, request):
        serializer = ConsultasSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(usuario=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        consulta = self.get_object()
        data_consulta = datetime(consulta.agenda.dia.year, consulta.agenda.dia.month, consulta.agenda.dia.day,
                                 consulta.horario.hora.hour, consulta.horario.hora.minute)
        if data_consulta < datetime.now():
            return Response(data={'erro': "Consulta já realizada, não é possível desmarcá-la."},
                            status=status.HTTP_400_BAD_REQUEST)
        consulta.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
