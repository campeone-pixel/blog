"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogapp/", include("blogapp.urls")),
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
