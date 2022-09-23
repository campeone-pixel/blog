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