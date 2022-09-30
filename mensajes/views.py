from contextlib import ContextDecorator
from unicodedata import category
from urllib import request
from django.shortcuts import render
from blogapp.models import *
from django.db.models import Count

from django.shortcuts import redirect

from mensajes.models import mensajes


def inbox_mensajes(request):
  inbox=mensajes.objects.filter(receiver= request.user)
  return render(request,"mensajes.html",{'inbox':inbox})

def send_mensajes(request):
  send=mensajes.objects.filter(sender= request.user)
  
  return render(request,"mensajes.html",{'send':send})

def create(request):
  pass

def buscar_usuario(request):
  pass
