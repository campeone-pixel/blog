from django.shortcuts import render
from blogapp.models import *
from blogapp.forms import *
from dataclasses import dataclass
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate



def inicio(request):
  posts = Post.objects.all()
  return render(request,'home.html',{'posts':posts})



#------------------------guardar-datos---------------------------------------------------------------------------------------------
"""def blogs(request):
  if request.method=='POST':
    form=form_blog(request.POST)
    if form.is_valid():
      information=form.cleaned_data
      id_blog=information['id_blog']
      titulo=information['titulo']
      creador=information['creador']
      
      guardar=blogs(id_blog=id_blog, titulo=titulo, creador=creador)
      guardar.save()
      formulario=form_blog()
      all_blogs = blogs.objects.all()
      return render(request, 'app_entrega1/blogs.html', {'formulario':formulario, 'all_blogs':all_blogs })
  else:
    formulario=form_blog()
    all_blogs = blogs.objects.all()
    return render(request, 'app_entrega1/blogs.html', {'formulario':formulario,
    'all_blogs':all_blogs})"""
"""
def guardar_proveedores(request):
  if request.method=='POST':
    form=proveedores_formularios(request.POST)
    if form.is_valid():
      information=form.cleaned_data
      proveedor_id=information['f_proveedor_id']
      nombre=information['f_nombre_proveedor']
      direccion=information['f_direccion_proveedor']
      cuit=information['f_cuit']
      guardar=proveedores(proveedor_id=proveedor_id, nombre_proveedor=nombre, direccion_proveedor=direccion,cuit=cuit)
      guardar.save()
      formulario=proveedores_formularios()
      all_proveedores = proveedores.objects.all()
      return render(request, 'app_entrega1/proveedores.html', {'formulario':formulario, 'all_proveedores':all_proveedores })
  else:
    formulario=proveedores_formularios()
    all_proveedores = proveedores.objects.all()
    return render(request, 'app_entrega1/proveedores.html', {'formulario':formulario,
    'all_proveedores':all_proveedores})
"""

#---------------------buscador------------------------------------------------------------------------------------------------  
def buscar_blog(request):
  

  if request.method=='POST':
    blog=request.POST['titulo']
    
    busqueda=blogs.objects.filter(titulo=blog)
    return render(request, 'app_entrega1/buscar_blog.html', {'all_blogs':busqueda })
  else:
    all_blogs= blogs.objects.all()
    return render(request, 'app_entrega1/buscar_blogs.html', {'all_blogs':all_blogs})


#-----------------------------------------------------------------------------------
"""

def eliminar_proveedor(request,proveedor_id):
  proveedor_a_borrar=proveedores.objects.get(proveedor_id=proveedor_id)
  proveedor_a_borrar.delete()
  all_proveedores = proveedores.objects.all()
  return render(request, 'app_entrega1/buscar_proveedores.html', {'all_proveedores':all_proveedores})

#------------------------------------------------------------------------------------------

def actualizar_proveedor(request,proveedor_id):
  proveedor=proveedores.objects.get(proveedor_id=proveedor_id)
  if request.method=='POST':
    formulario = proveedores_formularios(request.POST)
    if formulario.is_valid():
      producto_actualizado = formulario.cleaned_data
      proveedor.proveedor_id = producto_actualizado['f_proveedor_id']
      proveedor.nombre_proveedor = producto_actualizado['f_nombre_proveedor']
      proveedor.direccion_proveedor = producto_actualizado['f_direccion_proveedor']
      proveedor.cuit = producto_actualizado['f_cuit']
      proveedor.save()
      return render(request,'app_entrega1/buscar_proveedores.html')
  else:
    miformulario=proveedores_formularios(initial={'f_proveedor_id':proveedor.proveedor_id,'f_nombre_proveedor':proveedor.nombre_proveedor,'f_direccion_proveedor':proveedor.direccion_proveedor,'f_cuit':proveedor.cuit})
    return render( request, 'app_entrega1/actualizar_proveedor.html',{'miformulario':miformulario,'proveedor':proveedor})


#--------------------------------------------------------------------------------------------------------------------------

"""
def login_request(request):
  if request.method =="POST":
    form=AuthenticationForm(request,data = request.POST)

    if form.is_valid():
      usuario = form.cleaned_data.get("username")
      contra = form.cleaned_data.get("password")

      user= authenticate(username=usuario, password=contra)

      if user is not None:
        login(request,user)
        return render(request, "templates/inicio.html", {"mensaje":f"Bienvenido {usuario}"})

      else:
        return render(request, "templates/inicio.html", {"mensaje":"Error, datos incorrectos"})

  else:
        return render(request, "templates/inicio.html", {"mensaje":"Error, Formulario erroneo"})

  form = AuthenticationForm()

  return render(request, "templates/login.html", {"form":form})

#--------------------------------------------------------------------------------------------------------------------------
def register(request):
  if request.method =="POST":
    form = UserRegisterForm(request.POST)

    if form.is_valid():
      username = form.cleaned_data.get["username"]
      form.save()
      return render(request, "templates/inicio.html", {"mensaje":"{username} Usuario creado"})

  else:
    form=UserRegisterForm()

  return render(request, "templates/registro.html", {"form":form})

  
#--------------------------------------------------------------------------------------------------------------------------


























































