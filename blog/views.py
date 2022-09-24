from unicodedata import category
from django.shortcuts import render
from blogapp.models import *
from django.db.models import Count

def inicio(request):
  posts = Post.objects.filter(publicar= True)
  ultimos_posteos = Post.objects.order_by("fecha_creacion")[0:3]
  tags = Tag.objects.all()
  categorias= Category.objects.all().annotate(posts_count=Count('post'))
  return render(request,'home.html',{'posts':posts,'ultimos_posteos': ultimos_posteos,"tags":tags,'categorias':categorias})
  
def ver_articulo(request,slug):
  articulo = Post.objects.get(slug=slug)
  return render(request,'post-details.html',{'articulo':articulo})

def articulos_por_categoria(request,nombre):
  ultimos_posteos = Post.objects.order_by("fecha_creacion")[0:3]
  tags = Tag.objects.all()
  categorias= Category.objects.all().annotate(posts_count=Count('post'))
  categoria_a_filtrar= Category.objects.get(nombre = nombre)
  posts = Post.objects.filter(categoria= categoria_a_filtrar)
  
  return render(request,'home.html',{'posts':posts,'ultimos_posteos': ultimos_posteos,"tags":tags,'categorias':categorias})

def articulos_por_tag(request,nombre):
  ultimos_posteos = Post.objects.order_by("fecha_creacion")[0:3]
  tags = Tag.objects.all()
  categorias= Category.objects.all().annotate(posts_count=Count('post'))
  tag_a_filtrar= Tag.objects.get(nombre = nombre)
  posts = Post.objects.filter(tag= tag_a_filtrar)
  

  return render(request,'home.html',{'posts':posts,'ultimos_posteos': ultimos_posteos,"tags":tags,'categorias':categorias})


def articulos_buscados(request):
  ultimos_posteos = Post.objects.order_by("fecha_creacion")[0:3]
  tags = Tag.objects.all()
  categorias= Category.objects.all().annotate(posts_count=Count('post'))
  context = {} 
  
  if request.method == "GET": 
    query = request.GET.get("s") 
    posts = Post.objects.filter(titulo__icontains=query)
    if posts.count()==0:
      return render(request, "home.html", { 'ultimos_posteos': ultimos_posteos,"tags":tags,'categorias':categorias,'message':'No se encontraron resultados.'}) 
    else:
      return render(request, "home.html", { 'posts':posts,'ultimos_posteos': ultimos_posteos,"tags":tags,'categorias':categorias}) 