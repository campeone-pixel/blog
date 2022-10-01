
from unicodedata import category
from django.shortcuts import render
from blogapp.forms import Formulario_comment
from blogapp.models import *
from django.db.models import Count
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages





def login_request(request):
  if request.method =="POST":
    form=AuthenticationForm(request,data = request.POST)

    if form.is_valid():
      usuario = form.cleaned_data.get("username")
      contra = form.cleaned_data.get("password")

      user= authenticate(username=usuario, password=contra)

      if user is not None:
        login(request,user)
        return redirect("inicio")

      else:
        return render(request, "login.html", {"mensaje":"Error, datos incorrectos"})

  else:
    login_form = AuthenticationForm()
    return render(request, "login.html", {"login_form":login_form})

 
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("inicio")
  

def register(request):
    if request.method =="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso." )
            return redirect('inicio')
        messages.error(request, "Fallo el registro. Revise los datos suministrado.")
    else:		
        register_form=UserRegisterForm()
        return render(request, "register.html", {"register_form":register_form})


def profile (request):
  return render(request,'profile.html')