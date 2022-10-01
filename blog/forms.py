from dataclasses import fields
from turtle import width
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class form_blog(forms.Form):
  id_blog=forms.IntegerField()
  titulo=forms.CharField(max_length=50)
  creador=forms.CharField(max_length=50)
 
  



