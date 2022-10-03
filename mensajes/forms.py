from turtle import textinput
from django import forms
from tkinter import CASCADE
from ckeditor.fields import RichTextField
from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm

from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Formulario_mensaje(ModelForm):
    class Meta:
        model = Mensajes
        fields = ["sender", "receiver", "body"]
        widgets = {
            "sender": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "text",
                }
            ),
            "receiver": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "text",
                }
            ),
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "type": "text",
                }
            ),
        }
