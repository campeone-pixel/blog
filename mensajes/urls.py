from django.urls import path
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static
from mensajes.views import *

urlpatterns = [
  path('mensajes_recibidos/',mensajes_recibidos,name='mensajes_recibidos'),
  path('mensajes_enviados/',mensajes_enviados,name='mensajes_enviados'),
  path('crear_mensajes/',crear_mensajes,name='crear_mensajes'),
  path('crear_mensajes/<responder>', crear_mensajes, name='crear_mensajes'),  
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)