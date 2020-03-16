from django.db import models
from datetime import date
from django.core.exceptions import ValidationError

class Especialidades(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Medicos(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.IntegerField()
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    especialidade = models.ForeignKey(Especialidades, on_delete=models.CASCADE, related_name='especialidades')

    def __str__(self):
        return self.nome

class Horarios(models.Model):
    hora = models.TimeField()

    def __str__(self):
        return str(self.hora.strftime("%H:%M"))

class Agenda(models.Model):
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    dia = models.DateField()
    horarios = models.ManyToManyField(Horarios)
     
    class Meta:
        unique_together = ['medico','dia']
    
    def __str__(self):
        return '%s - %s' % (self.medico, self.dia)

    def clean(self):
        if self.dia < date.today():
            raise ValidationError({'dia':('Data da agenda não pode ser anterior ao dia corrente.')})
           



