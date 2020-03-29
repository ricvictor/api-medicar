from django.contrib import admin

from gerenciamento.models import (Agenda, Consultas, Especialidades, Horarios,
                                  Medicos)

# Register your models here.
admin.site.register(Especialidades)
admin.site.register(Medicos)
admin.site.register(Horarios)
admin.site.register(Agenda)
admin.site.register(Consultas)
