from turtle import textinput
from .models import *
from django.forms import ModelForm
from .models import Post, Tag, Category, Escritor, Comment
from django.forms import ModelForm, Textarea


class Formulario_comentario(ModelForm):
    class Meta:
        model = Comment
        fields = ("contenido",)

        widgets = {
            "contenido": Textarea(
                attrs={
                    "cols": 20,
                    "rows": 5,
                    "class": "form-control col-10",
                    "id": "text",
                    "placeholder": "Escriba su comentario aqui",
                }
            ),
        }


class Formulario_post(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["me_gusta", "fecha_creacion"]
