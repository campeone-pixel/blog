from django.shortcuts import render
from blogapp.models import *

def inicio(request):
  posts = Post.objects.all()
  return render(request,'home.html',{'posts':posts})