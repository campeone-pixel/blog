from django.contrib import admin
from django.urls import path, include
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static
from re import template
from django.contrib.auth.views import LogoutView
from .views import *


urlpatterns = [
  
    path("iniciar_sesion/",iniciar_sesion, name='iniciar_sesion'),
    path("registro/",registro, name='registro'),
    path("cerrar_sesion/",cerrar_sesion, name='cerrar_sesion'),
    path("editar_perfil/",editar_perfil, name='editar_perfil'),
    path("cambiar_contrasenia/",cambiar_contrasenia, name='cambiar_contrasenia'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
