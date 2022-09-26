from django.contrib import admin
from django.urls import path, include
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static
from mensajes.views import *


urlpatterns = [
  path('',index_mensajes,name='index_mensajes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)