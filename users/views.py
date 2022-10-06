from django.shortcuts import render
from blogapp.models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import *


def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return redirect("inicio")
        else:
            messages.success(request, "Datos incorrectos.")
            return redirect("registro")
    else:
        login_form = AuthenticationForm()
        return render(request, "login.html", {"login_form": login_form})

@login_required()
def cerrar_sesion(request):
    logout(request)
    messages.info(request, "Cerraste sesion")
    return redirect("inicio")


def registro(request):
    if request.method == "POST":
        form = form_registro(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, "Registro exitoso.")
            return redirect("inicio")
        else:
            messages.success(request, "Registro incorrecto.")
            return redirect("registro")
    else:
        register_form = form_registro()
        return render(request, "register.html", {"register_form": register_form})


@login_required
def editar_perfil(request):
    if request.method == "POST":
        u_form = form_act_usuario(request.POST, instance=request.user)
        p_form = form_act_perfil(
            request.POST, request.FILES, instance=request.user.perfil
        )
        if "email" in request.POST:
            u_form = form_act_usuario(request.POST, instance=request.user)
            u_form.save()
            messages.success(request, f"Tu cuenta ha sido actualizada")
            return redirect("editar_perfil")
        if p_form.is_valid:
            p_form.save()
            messages.success(request, f"Tu cuenta ha sido actualizada")
            return redirect("editar_perfil")
        messages.success(request, "Datos incorrecto.")
        return redirect("registro")
    else:
        u_form = form_act_usuario(instance=request.user)
        p_form = form_act_perfil(instance=request.user.perfil)
    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "all_profile.html", context)

@login_required()
def cambiar_contrasenia(request):
    if request.method == "POST":
        cambio_contrasenia = form_cambio_contrasenia(request.user, request.POST)
        if cambio_contrasenia.is_valid():
            cambio_contrasenia.save()
            update_session_auth_hash(request, cambio_contrasenia.user)
            messages.success(request, "Tu contrasenia ha sido modificada exitosamente")
            return redirect("cambiar_contrasenia")
        else:
            messages.error(request, "Tu contrasenia no fue actualizada")
            return redirect("cambiar_contrasenia")
    else:
        change_pass = form_cambio_contrasenia(request.user)
        return render(request, "all_profile.html", {"change_pass": change_pass})
