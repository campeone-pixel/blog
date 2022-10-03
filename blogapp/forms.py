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

from django.forms import ModelForm, Textarea,TextInput,ImageField,BooleanField,DateField,SlugField

class Formulario_comment(ModelForm):
        class Meta:
            model = Comment
            fields = ('contenido',)

            widgets = {
            'contenido': Textarea(attrs={
                'cols': 20, 'rows': 5,
                'class': "form-control col-10",
                'id':'text',
                
                'placeholder': 'Escriba su comentario aqui',

                
                }),
            
        }


class Formulario_post(ModelForm):
  class Meta:
      model = Post
      fields = '__all__'
      exclude = ['me_gusta','fecha_creacion']

