from unicodedata import category
from urllib import request
from django.shortcuts import render
from blogapp.models import *
from .forms import Formulario_post
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test




@login_required()
@user_passes_test(lambda user: user.is_superuser , login_url='/')
def ver_posts(request):
    all_posts = Post.objects.all()
    form = Formulario_post()
    return render(
        request, "crud.html", {"all_posts": all_posts, "form": form, "ver_posts": True}
    )

@login_required()
@user_passes_test(lambda user: user.is_superuser , login_url='/')
def agregar_post(request):
    if request.method == "POST":
        form = Formulario_post(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "El post fue guardado exitosamente.")
            return redirect("ver_posts")

        else:
            messages.error(
                request,
                "El post NO fue guardado exitosamente. Revise los datos enviados",
            )

            return redirect("ver_posts")
    else:
        return redirect("ver_posts")

@login_required()
@user_passes_test(lambda user: user.is_superuser , login_url='/')
def actualizar_post(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
        form = Formulario_post(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "El post fue editado exitosamente.")
            return redirect("ver_posts")
    else:
        update_form = Formulario_post(instance=post)
        return render(request, "crud.html", {"update_form": update_form, "post": post})

@login_required()
@user_passes_test(lambda user: user.is_superuser , login_url='/')
def borrar_post(request, slug):
    post_delete = Post.objects.get(slug=slug)
    if request.method == "POST":
        post_delete.delete()
        return redirect("ver_posts")
    else:
        return render(request, "crud.html", {"post_delete": post_delete})

@login_required()
@user_passes_test(lambda user: user.is_superuser , login_url='/')
def buscar_posts(request):
    if request.method == "GET":
        busqueda = request.GET.get("s")
        search_post = Post.objects.filter(titulo__icontains=busqueda)
        contexto = {"ver_posts": True}
        if search_post.count() != 0:
            contexto["all_posts"] = search_post
            return render(request, "crud.html", contexto)
        else:
            messages.success(request, "No se encontraron resultados segun la busqueda")
            return redirect("ver_posts")
