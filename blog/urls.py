from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogapp/", include("blogapp.urls")),
    path("mensajes/", include("mensajes.urls")),
    path("users/", include("users.urls")),
    path("", inicio, name="inicio"),
    path("ver_articulo/<slug>/", ver_articulo, name="ver_articulo"),
    path(
        "articulos_por_categoria/<slug:slug>/",
        articulos_por_categoria,
        name="articulos_por_categoria",
    ),
    path("articulos_por_tag/<slug:slug>/", articulos_por_tag, name="articulos_por_tag"),
    path("articulos_buscados/", articulos_buscados, name="articulos_buscados"),
    path("sobre_nosotros/", sobre_nosotros, name="sobre_nosotros"),
    path('__debug__/', include('debug_toolbar.urls')),
    path("ver_perfil/<usuario>", ver_perfil, name="ver_perfil"),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
