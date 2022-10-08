from pathlib import Path
from django.contrib import admin
from django.urls import path
from .views import *
from re import template
from django.contrib.auth.views import LogoutView
urlpatterns = [
  path( 'ver_posts/',ver_posts,name='ver_posts'),
  path( 'agregar_post/',agregar_post,name='agregar_post'),
  path( 'actualizar_post/<slug:slug>',actualizar_post,name='actualizar_post'),
  path( 'borrar_post/<slug:slug>',borrar_post,name='borrar_post'),
  path( 'buscar_posts/',buscar_posts,name='buscar_posts'),
 
]
