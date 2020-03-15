from django.db import models

class Especialidades(models.Model):
    nome = models.CharField(max_length=100, unique=True)

class Medicos(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.IntegerField()
    email = models.EmailField(null=True)
    telefone = models.CharField(max_length=20, null=True)
    especialidade = models.ForeignKey(Especialidades, on_delete=models.CASCADE, null=True)

class Horarios(models.Model):
    hora = models.TimeField()

class Agenda(models.Model):
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE, null=True)
    dia = models.DateField()
    horarios = models.ManyToManyField(Horarios)

