from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil


class form_registro(UserCreationForm):
    

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class form_act_usuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "inputFirstName",
                    "type": "text",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "inputLastName",
                    "type": "text",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "id": "inputEmailAddress",
                    "type": "email",
                }
            ),
        }


class form_act_perfil(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["imagen"]


class form_cambio_contrasenia(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget = forms.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["new_password1"].widget = forms.PasswordInput(
            attrs={"class": "form-control"}
        )
        self.fields["new_password2"].widget = forms.PasswordInput(
            attrs={"class": "form-control"}
        )
