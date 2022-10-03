from django.contrib import admin
from django.urls import path, include
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static
from re import template
from django.contrib.auth.views import LogoutView
from .views import *


urlpatterns = [
  
    path("login_request/",login_request, name='login_request'),
    path("register/",register, name='register'),
    path("logout/",logout_request, name='logout'),
    path("edit_profile/",edit_profile, name='edit_profile'),
    path("change_pass/",change_pass, name='change_pass'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
