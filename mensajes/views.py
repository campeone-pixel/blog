from contextlib import ContextDecorator
from unicodedata import category
from urllib import request
from django.shortcuts import render
from blogapp.models import *
from django.db.models import Count

from django.shortcuts import redirect

from mensajes.forms import Formulario_mensaje
from .models import Mensajes


def inbox_mensajes(request):
    inbox = Mensajes.objects.filter(receiver=request.user)
    return render(request, "all_profile.html", {"inbox": inbox})


def send_mensajes(request):
    send = Mensajes.objects.filter(sender=request.user)

    return render(request, "all_profile.html", {"send": send})


def create(request):

    if request.method == "POST":
        form_new_message = Formulario_mensaje(request.POST)
        
        if form_new_message.is_valid:

            form_new_message.save()
            return redirect("inicio")

        else:
            return redirect("create")

    else:
        form_new_message = Formulario_mensaje(initial={'sender': request.user})
        

        return render(
            request, "all_profile.html", {"form_new_message": form_new_message}
        )


def buscar_usuario(request):
    pass
