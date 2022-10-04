from contextlib import ContextDecorator
from email.message import Message
from unicodedata import category
from urllib import request
from django.dispatch import receiver
from django.shortcuts import render
from blogapp.models import *
from django.db.models import Count

from django.shortcuts import redirect

from mensajes.forms import Formulario_mensaje
from .models import Mensajes
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


def inbox_mensajes(request):
    inbox = Mensajes.objects.filter(receiver=request.user)
    return render(request, "all_profile.html", {"inbox": inbox})


def send_mensajes(request):
    send = Mensajes.objects.filter(sender=request.user)

    return render(request, "all_profile.html", {"send": send})


def create_func():
    pass


def create(request, responder=None):
    if responder == None:
        if request.method == "POST":

            receiver = request.POST["receiver"]
            body = request.POST["body"]
            try:
                receiver_user = User.objects.get(username=receiver)
                nuevo_mensaje = Mensajes.objects.create(
                    sender=request.user, receiver=receiver_user, body=body
                )
                nuevo_mensaje.save()
                return redirect("send_mensajes")
            except ObjectDoesNotExist:
                messages.error(request, "El usuario no existe.")
                return redirect("create")

        else:
            form_new_message = Formulario_mensaje(initial={"sender": request.user})
            return render(
                request, "all_profile.html", {"form_new_message": form_new_message}
            )
    else:
        if request.method == "POST":
            receiver = request.POST["receiver"]
            body = request.POST["body"]
            try:
                receiver_user = User.objects.get(username=receiver)
                nuevo_mensaje = Mensajes.objects.create(
                    sender=request.user, receiver=receiver_user, body=body
                )
                nuevo_mensaje.save()
                return redirect("send_mensajes")
            except ObjectDoesNotExist:
                messages.error(request, "El usuario no existe.")
                return redirect("create")

        else:
            form_new_message = Formulario_mensaje(
                initial={"sender": request.user, "receiver": responder}
            )
            return render(
                request, "all_profile.html", {"form_new_message": form_new_message}
            )


def buscar_usuario(request):
    pass
