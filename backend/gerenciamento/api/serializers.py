from rest_framework.serializers import ModelSerializer
from gerenciamento.models import Especialidades, Medicos, Horarios, Agenda
from rest_framework.validators import UniqueTogetherValidator

class EspecialidadesSerializer(ModelSerializer):
    class Meta:
        model = Especialidades
        fields = ['nome']

class MedicosSerializer(ModelSerializer):
    especialidades = EspecialidadesSerializer()

    class Meta:
        model = Medicos
        fields = ['nome','crm','especialidades']

class HorariosSerializer(ModelSerializer):
    class Meta:
        model = Horarios
        fields = ['hora']

class AgendaSerializer(ModelSerializer):
    medico = MedicosSerializer()
    horarios = HorariosSerializer(many=True)

    class Meta:
        model = Agenda
        fields = ['medico','dia','horarios']
        validators = [
            UniqueTogetherValidator(
                queryset=Agenda.objects.all(),
                fields=['medico', 'dia']
            )
        ]