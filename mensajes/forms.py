from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User


class Formulario_mensaje(ModelForm):
    class Meta:
        model = Mensajes
        fields = ["enviado_por", "recibido_por", "cuerpo"]
        widgets = {
            "enviado_por": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "text",
                }
            ),
            "recibido_por": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "text",
                }
            ),
            "cuerpo": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "type": "text",
                }
            ),
        }
