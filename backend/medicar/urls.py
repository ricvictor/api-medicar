"""medicar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

# viewsets
from gerenciamento.api import viewsets

router = routers.DefaultRouter()
router.register(r'especialidades', viewsets.EspecialidadesViewSet, basename='especialidades')
router.register(r'medicos', viewsets.MedicosViewSet, basename='medicos')
router.register(r'agendas', viewsets.AgendaViewSet, basename='agendas')
router.register(r'consultas', viewsets.ConsultasViewSet, basename='consultas')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path(r'account/', include('rest_auth.urls')),
    path(r'account/registration/', include('rest_auth.registration.urls')),
]
