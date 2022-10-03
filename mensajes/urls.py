from django.contrib import admin
from django.urls import path, include
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static
from mensajes.views import *


urlpatterns = [
  path('inbox_mensajes/',inbox_mensajes,name='inbox_mensajes'),
  path('send_mensajes/',send_mensajes,name='send_mensajes'),
  path('create/',create,name='create'),
  path('create/<responder>', create, name='create'),  
  
  
  path('buscar_usuario/',buscar_usuario,name='buscar_usuario'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)