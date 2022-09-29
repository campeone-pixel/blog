from contextlib import ContextDecorator
from unicodedata import category
from django.shortcuts import render
from blogapp.models import *
from django.db.models import Count

from django.shortcuts import redirect


def index_mensajes(request):
  return render(request,"mensajes.html")