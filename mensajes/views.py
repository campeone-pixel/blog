from django.shortcuts import render
from blogapp.models import *
from django.shortcuts import redirect
from mensajes.forms import Formulario_mensaje
from .models import Mensajes
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


def mensajes_recibidos(request):
    inbox = Mensajes.objects.filter(recibidio_por=request.user)
    return render(request, "all_profile.html", {"inbox": inbox})


def mensajes_enviados(request):
    send = Mensajes.objects.filter(sender=request.user)

    return render(request, "all_profile.html", {"send": send})



def crear_mensajes(request, responder=None):
    if responder == None:
        if request.method == "POST":
            recibidio_por = request.POST["recibidio_por"]
            cuerpo = request.POST["cuerpo"]
            try:
                obj_recibido_por = User.objects.get(username=recibidio_por)
                nuevo_mensaje = Mensajes.objects.create(
                    enviado_por=request.user, recibido_por=obj_recibido_por, cuerpo=cuerpo
                )
                nuevo_mensaje.save()
                return redirect("mensajes_enviados")
            except ObjectDoesNotExist:
                messages.error(request, "El usuario no existe.")
                return redirect("crear_mensajes")

        else:
            form_nuevo_mensaje = Formulario_mensaje(initial={"enviado_por": request.user})
            return render(
                request, "all_profile.html", {"form_nuevo_mensaje": form_nuevo_mensaje}
            )
    else:
        if request.method == "POST":
            recibidio_por = request.POST["recibidio_por"]
            cuerpo = request.POST["cuerpo"]
            try:
                obj_recibido_por = User.objects.get(username=recibidio_por)
                nuevo_mensaje = Mensajes.objects.create(
                    enviado_por=request.user, recibido_por=obj_recibido_por, cuerpo=cuerpo
                )
                nuevo_mensaje.save()
                return redirect("mensajes_enviados")
            except ObjectDoesNotExist:
                messages.error(request, "El usuario no existe.")
                return redirect("crear_mensajes")
        else:
            form_nuevo_mensaje = Formulario_mensaje(
                initial={"enviado_por": request.user, "recibido_por": responder}
            )
            return render(
                request, "all_profile.html", {"form_nuevo_mensaje": form_nuevo_mensaje}
            )


