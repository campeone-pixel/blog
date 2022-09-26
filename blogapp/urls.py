from pathlib import Path
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
  path( 'CRUD/',CRUD,name='CRUD'),
  path( 'agregar_post/',agregar_post,name='agregar_post'),
  path( 'eliminar_post/<slug>/',eliminar_post,name='eliminar_post'),
  path( 'editar_post/<slug>/',editar_post,name='editar_post'),
  path( 'buscar_post/filtro/',buscar_post,name='buscar_post'),
]
