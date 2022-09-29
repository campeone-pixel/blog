
from unicodedata import category
from django.shortcuts import render
from blogapp.forms import Formulario_comment
from blogapp.models import *
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from .forms import *

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
        new_comment= Comment.objects.create(post = articulo,contenido = contenido)
        new_comment.save()
        form=Formulario_comment()
        return render(request, "home.html", {"articulo": articulo,'all_comments':all_comments, 'form':form})
      else:
        form=Formulario_comment()
        return render(request, "home.html", {"articulo": articulo,'all_comments':all_comments, 'form':form})

    else:
      form=Formulario_comment()
      return render(request, "home.html", {"articulo": articulo,'all_comments':all_comments, 'form':form})

def login_request(request):
  if request.method =="POST":
    form=AuthenticationForm(request,data = request.POST)

    if form.is_valid():
      usuario = form.cleaned_data.get("username")
      contra = form.cleaned_data.get("password")

      user= authenticate(username=usuario, password=contra)

      if user is not None:
        login(request,user)
        return render(request, "login.html", {"mensaje":f"Bienvenido {usuario}"})

      else:
        return render(request, "login.html", {"mensaje":"Error, datos incorrectos"})

  else:
        return render(request, "login.html", {"mensaje":"Error, Formulario erroneo"})

  form = AuthenticationForm()

  return render(request, "login.html", {"form":form})

#--------------------------------------------------------------------------------------------------------------------------
def register(request):
  if request.method =="POST":
    form = UserRegisterForm(request.POST)

    if form.is_valid():
      username = form.cleaned_data.get["username"]
      form.save()
      return render(request, "register.html", {"mensaje":f"{username} Usuario creado"})

  else:
    form=UserRegisterForm()

    return render(request, "register.html", {"form":form})
