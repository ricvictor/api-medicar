# standard library
from datetime import date, datetime

# Django, django-rest
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.serializers import (DateField, IntegerField,
                                        ModelSerializer, StringRelatedField,
                                        TimeField, ValidationError)

# models
from gerenciamento.models import (Agenda, Consultas, Especialidades, Horarios,
                                  Medicos)


class EspecialidadesSerializer(ModelSerializer):

    class Meta:
        model = Especialidades
        fields = ['id', 'nome']


class MedicosSerializer(ModelSerializer):
    especialidade = EspecialidadesSerializer(read_only=True)

    class Meta:
        model = Medicos
        fields = ['id', 'nome', 'crm', 'especialidade']


class AgendaSerializer(ModelSerializer):
    medico = MedicosSerializer(read_only=True)
    horarios = StringRelatedField(many=True)

    class Meta:
        model = Agenda
        fields = ['id', 'medico', 'dia', 'horarios']


class ConsultasSerializer(ModelSerializer):
    agenda_id = IntegerField(write_only=True)
    dia = DateField(source='agenda.dia', read_only=True)
    horario = TimeField(source='horario.hora', format="%H:%M")
    medico = MedicosSerializer(source='agenda.medico', read_only=True)

    def validate_horario(self, value):
        try:
            hora = value
            horario = Horarios.objects.get(hora=hora)
            return value
        except ObjectDoesNotExist:
            raise ValidationError('Horario não existe.')

    def validate_agenda_id(self, value):
        try:
            agenda = Agenda.objects.get(id=value)
            return value
        except ObjectDoesNotExist:
            raise ValidationError('Agenda não existe.')

    def create(self, validated_data):
        usuario = validated_data['usuario']
        hora = validated_data['horario']
        horario = Horarios.objects.get(hora=hora['hora'])
        agenda = Agenda.objects.get(id=validated_data['agenda_id'])
        data_consulta = datetime(agenda.dia.year, agenda.dia.month, agenda.dia.day,
                                 horario.hora.hour, horario.hora.minute)
        if data_consulta < datetime.now():
            raise ValidationError('Data e horário da consulta não podem ser retroativos.')
        if Consultas.objects.filter(usuario=usuario, agenda=agenda, horario=horario).exists():
            raise ValidationError('Consulta já foi mercada pelo usuário. Verificar na lista de consultas.')
        if Consultas.objects.filter(agenda=agenda, horario=horario).exists():
            raise ValidationError(
                'Consulta já foi mercada por outra pessoa. Verificar novamente a lista de agendas disponíveis.')

        consulta = Consultas.objects.create(agenda=agenda, horario=horario, usuario=usuario)

        return consulta

    class Meta:
        model = Consultas
        fields = ['id', 'dia', 'agenda_id', 'horario', 'data_agendamento', 'medico']
