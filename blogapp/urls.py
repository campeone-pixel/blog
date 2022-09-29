from pathlib import Path
from django.contrib import admin
from django.urls import path
from .views import *
from re import template
from django.contrib.auth.views import LogoutView
urlpatterns = [
  path( 'CRUD/',CRUD,name='CRUD'),
  path( 'agregar_post/',agregar_post,name='agregar_post'),
  path( 'eliminar_post/<slug>/',eliminar_post,name='eliminar_post'),
  path( 'editar_post/<slug>/',editar_post,name='editar_post'),
  path( 'buscar_post/filtro/',buscar_post,name='buscar_post'),
  path("login",login_request, name='login'),
  path("register",register, name='register'),
  path("logout",LogoutView.as_view(template_name="app_entrega1/logout.html"), name='logout'),
]
