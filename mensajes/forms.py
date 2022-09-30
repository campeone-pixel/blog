from turtle import textinput
from django import forms
from tkinter import CASCADE
from ckeditor.fields import RichTextField
from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post,Tag,Category,Escritor,Comment
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Formulario_mensaje(forms.Form):
  class Meta:
      model = Post
      fields = '__all__'
      