from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .forms import LoginForm




# Create your views here.

def crear_usuario(request):
    
    

def iniciar_sesion(request):
    mensaje = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            user = authenticate(request, username=usuario, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return render(request,"login.html", 
                              {"form":form, "mensaje":"Credenciales incorrectas"})
            
        
       

def guardar_nombre(request):
   request.session['nombre_usuario'] = 'Invitado'
   return HttpResponse("El nombre del usuario ha sido almacenado.")

def leer_nombre(request):
   nombre = request.session.get('nombre_usuario', 'No existe este usuario.')
   return HttpResponse(f"Usuario: {nombre}")

def eliminar_nombre(request):
   if 'nombre_usuario' in request.session:
       del request.session['nombre_usuario']
       return HttpResponse("El nombre del usuario ha sido eliminado.")

def limpiar_sesion(request):
   request.session.flush()
   return HttpResponse("Se ha eliminado toda la sesion.")


def contador_visitas(request):
   visitas = request.session.get('visitas', 0)
   visitas += 1
   request.session['visitas'] = visitas
   return render(request,"contador.html", {"visitas":visitas})