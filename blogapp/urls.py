from pathlib import Path
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
  path( 'ver_posts/',ver_posts,name='ver_posts'),
  path( 'agregar_post/',agregar_post,name='agregar_post'),
  path( 'update_post/<slug:slug>',update_post,name='update_post'),
  path( 'delete_post/<slug:slug>',delete_post,name='delete_post'),
  path( 'search_posts/',search_posts,name='search_posts'),
 
]
