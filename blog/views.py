from django.shortcuts import render
from blogapp.forms import Formulario_comentario
from blogapp.models import *
from django.db.models import Count
from django.contrib.auth.models import User
from users.models import Perfil
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def datos_sidebar():
    ultimos_posteos = Post.objects.order_by("fecha_creacion").order_by(
        "-fecha_creacion",
    )[0:3]
    tags = Tag.objects.all().order_by(
        "-fecha_creacion",
    )
    categorias = (
        Category.objects.all()
        .annotate(posts_count=Count("posts"))
        .order_by(
            "-fecha_creacion",
        )
    )
    inicio = "inicio"
    return {
        "ultimos_posteos": ultimos_posteos,
        "tags": tags,
        "categorias": categorias,
        "inicio": inicio,
    }


# ----------------------------------------------------------------------#
#                            VISTAS - HOME                             #
# ----------------------------------------------------------------------#


def inicio(request):
    todos_los_posts = Post.objects.all().order_by(
        "-fecha_creacion",
    )

  
    if todos_los_posts.count() == 0:
        mensajes = "No hay articulos para mostrar"
        contexto = {
            "todos_los_posts": todos_los_posts,
            "mensajes": mensajes,
        }
        contexto.update(datos_sidebar())
        return render(request, "home.html", contexto)
    else:
        contexto = {"todos_los_posts": todos_los_posts}
        contexto.update(datos_sidebar())
        return render(request, "home.html", contexto)
  


def articulos_por_categoria(request, slug):
    categoria_a_filtrar = Category.objects.get(slug=slug)
    articulos_por_categoria = Post.objects.filter(
        categoria=categoria_a_filtrar
    ).order_by(
        "-fecha_creacion",
    )
    if articulos_por_categoria.count() == 0:
        mensajes = "No hay articulos correspondiente a la categoria seleccionada"
        contexto = {
            "articulos_por_categoria": articulos_por_categoria,
            "mensajes": mensajes,
        }
        contexto.update(datos_sidebar())
        return render(request, "home.html", contexto)
    else:
        contexto = {
            "articulos_por_categoria": articulos_por_categoria,
        }
        contexto.update(datos_sidebar())
        return render(request, "home.html", contexto)


def articulos_por_tag(request, slug):
    tag_a_filtrar = Tag.objects.get(slug=slug)
    articulos_por_tag = Post.objects.filter(tag=tag_a_filtrar).order_by(
        "-fecha_creacion",
    )
    if articulos_por_tag.count() == 0:
        mensajes = "No hay articulos correspondiente con el tag seleccionado"
        contexto = {"articulos_por_tag": articulos_por_tag, "mensajes": mensajes}
        contexto.update(datos_sidebar())
        return render(request, "home.html", contexto)
    else:
        contexto = {
            "articulos_por_tag": articulos_por_tag,
        }
        contexto.update(datos_sidebar())
        return render(request, "home.html", contexto)


def articulos_buscados(request):
    if request.method == "GET":
        busqueda = request.GET.get("s")
        articulos_buscados = Post.objects.filter(titulo__icontains=busqueda).order_by(
            "-fecha_creacion",
        )
        contexto = datos_sidebar()
        if articulos_buscados.count() != 0:
            contexto["articulos_buscados"] = articulos_buscados
            return render(request, "home.html", contexto)
        else:
            contexto["mensajes"] = "No se encontraron resultados."
            return render(request, "home.html", contexto)


def sobre_nosotros(request):
    contexto = {"sobre_nosotros": "sobre_nosotros"}
    return render(request, "home.html", contexto)


def ver_articulo(request, slug):
    articulo = Post.objects.get(slug=slug)

    todos_los_comentarios = Comment.objects.filter(post=articulo)

    form = Formulario_comentario()
    return render(
        request,
        "home.html",
        {
            "articulo": articulo,
            "todos_los_comentarios": todos_los_comentarios,
            "form": form,
        },
    )


@login_required()
def enviar_comentario(request, slug):
    articulo = Post.objects.get(slug=slug)
    form_comentario = Formulario_comentario(data=request.POST)
    if form_comentario.is_valid():
        form_data = form_comentario.cleaned_data
        contenido = form_data.get("contenido")
        nuevo_comentario = Comment.objects.create(
            post=articulo, contenido=contenido, autor=request.user
        )
        nuevo_comentario.save()
        form = Formulario_comentario()
        return redirect("ver_articulo", articulo.slug)
    else:
        return redirect("ver_articulo", articulo.slug)


def ver_perfil(request, usuario):

    ver_usuario = User.objects.get(id=usuario)
    ver_perfil = Perfil.objects.get(usuario=usuario)
    return render(
        request, "home.html", {"ver_perfil": ver_perfil, "ver_usuario": ver_usuario}
    )
