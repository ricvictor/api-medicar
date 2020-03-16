from rest_framework.viewsets import ModelViewSet
from gerenciamento.models import Especialidades, Medicos, Horarios, Agenda
from .serializers import EspecialidadesSerializer, MedicosSerializer, HorariosSerializer, AgendaSerializer

class EspecialidadesViewSet(ModelViewSet):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer

class MedicosViewSet(ModelViewSet):
    queryset = Medicos.objects.all()
    serializer_class = MedicosSerializer

class AgendaViewSet(ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer