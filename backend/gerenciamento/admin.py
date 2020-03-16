from django.contrib import admin
from gerenciamento.models import Especialidades, Medicos, Horarios, Agenda

# Register your models here.
admin.site.register(Especialidades)
admin.site.register(Medicos)
admin.site.register(Horarios)
admin.site.register(Agenda)
