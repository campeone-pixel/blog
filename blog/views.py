
from unicodedata import category
from django.shortcuts import render
from blogapp.forms import Formulario_comment
from blogapp.models import *
from django.db.models import Count
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages





def datos_sidebar():
    ultimos_posteos = Post.objects.order_by("fecha_creacion")[0:3]
    tags = Tag.objects.all()
    categorias = Category.objects.all().annotate(posts_count=Count("posts"))
    inicio="inicio"
    return {"ultimos_posteos": ultimos_posteos, "tags": tags, "categorias": categorias,'inicio':inicio}


# ----------------------------------------------------------------------#
#                            VISTAS - HOME                             #
# ----------------------------------------------------------------------#


def inicio(request):
    all_posts = Post.objects.all()
    contexto = {"all_posts": all_posts}
    contexto.update(datos_sidebar())
    return render(request, "home.html", contexto)


def articulos_por_categoria(request, slug):
    categoria_a_filtrar = Category.objects.get(slug=slug)
    articulos_por_categoria = Post.objects.filter(categoria=categoria_a_filtrar)
    contexto = {
        "articulos_por_categoria": articulos_por_categoria,
    }
    contexto.update(datos_sidebar())
    return render(request, "home.html", contexto)


def articulos_por_tag(request, slug):
    tag_a_filtrar = Tag.objects.get(slug=slug)
    articulos_por_tag = Post.objects.filter(tag=tag_a_filtrar)
    contexto = {
        "articulos_por_tag": articulos_por_tag,
    }
    contexto.update(datos_sidebar())
    return render(request, "home.html", contexto)


def articulos_buscados(request):
    if request.method == "GET":
        busqueda = request.GET.get("s")
        articulos_buscados = Post.objects.filter(titulo__icontains=busqueda)
        contexto = datos_sidebar()
        if articulos_buscados.count() != 0:
            contexto["articulos_buscados"] = articulos_buscados
            return render(request, "home.html", contexto)
        else:
            contexto["message"] = "No se encontraron resultados."
            return render(request, "home.html", contexto)


def sobre_nosotros(request):
  contexto= {'sobre_nosotros':'sobre_nosotros'}
  return render(request, "home.html", contexto)


def ver_articulo(request, slug):
    articulo = Post.objects.get(slug=slug)
    
    all_comments = Comment.objects.filter(post=articulo)
    if request.method == 'POST':
      form_comment= Formulario_comment(data=request.POST)
      if form_comment.is_valid():
        form_data= form_comment.cleaned_data
        contenido= form_data.get('contenido')
        new_comment= Comment.objects.create(post = articulo,contenido = contenido,autor=request.user)
        new_comment.save()
        form=Formulario_comment()
        return render(request, "home.html", {"articulo": articulo,'all_comments':all_comments, 'form':form})
      else:
        form=Formulario_comment()
        return render(request, "home.html", {"articulo": articulo,'all_comments':all_comments, 'form':form})

    else:
      form=Formulario_comment()
      return render(request, "home.html", {"articulo": articulo,'all_comments':all_comments, 'form':form})

def ver_profile(request,usuario):
    
    ver_usuario=User.objects.get(id=usuario)
    ver_perfil=Profile.objects.get(user=usuario)
    return render(request, 'home.html',{"ver_perfil":ver_perfil,'ver_usuario':ver_usuario})


