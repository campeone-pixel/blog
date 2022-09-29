from contextlib import ContextDecorator
from unicodedata import category
from django.shortcuts import render
from blogapp.models import *
from django.db.models import Count
from .forms import Formulario_post
from django.shortcuts import redirect


def CRUD(request):
  posts = Post.objects.all()
  form=Formulario_post()
  return render(request,'CRUD.html',{'posts':posts,'form':form})


def agregar_post(request):
  if request.method=='POST':
    form = Formulario_post(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('CRUD')
    else:
      return redirect('CRUD')

def editar_post(request,slug):
  if request.method=='POST':
    form = Formulario_post(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('CRUD')
    else:
      form
      return redirect('CRUD')


def eliminar_post(request,slug):
  pass


def buscar_post(request,nombre):
  pass

