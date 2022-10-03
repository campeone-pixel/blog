from unicodedata import category
from django.shortcuts import render

from blogapp.models import *

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return redirect("inicio")

        else:
 
            messages.success(request, 'Datos incorrectos.')
            return redirect('register')


    else:
        login_form = AuthenticationForm()
        return render(request, "login.html", {"login_form": login_form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("inicio")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso.")
            return redirect("inicio")
        else:
            messages.success(request, 'Registro incorrecto.')
            return redirect('register')
            
    else:
        register_form = UserRegisterForm()
        return render(request, "register.html", {"register_form": register_form})


@login_required
def edit_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        
        
        if 'email' in request.POST:
            u_form = UserUpdateForm(request.POST, instance=request.user)
            u_form.save()
            
            messages.success(request, f"Tu cuenta ha sido actualizada")
            return redirect("edit_profile")


        if  p_form.is_valid:
           
            p_form.save()
            messages.success(request, f"Tu cuenta ha sido actualizada")
            return redirect("edit_profile")
        
              
        messages.success(request, 'Datos incorrecto.')
        return redirect('register')

    else:
        
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}

    return render(request, "all_profile.html", context)

def change_pass(request):
    if request.method == 'POST':
        change_pass = MyPasswordChangeForm(request.user, request.POST)
        if change_pass.is_valid():
            change_pass.save()
            
            update_session_auth_hash(request, change_pass.user)
            messages.success(request, 'Tu contrasenia ha sido modificada exitosamente')
            
        else:
            
            messages.error(request, 'Tu contrasenia no fue actualizada')
            return redirect('change_pass')
    else:
        change_pass = MyPasswordChangeForm(request.user)
        return render(request, 'all_profile.html', {
        'change_pass': change_pass
    })


