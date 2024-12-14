from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Auto
from .forms import AutoForm
from .models import Usuario
from .forms import UsuarioForm
from .models import Empleado
from .forms import EmpleadoForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})
def empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/empleados.html', {'empleados': empleados})
def autos(request):
    autos = Auto.objects.all()
    return render(request, 'autos/index.html', {'autos': autos})


#CRUD AUTO

def crear_auto(request):
    #Request FILE recepciona archivos
    formulario = AutoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid(): #Recepcionar datos
        formulario.save() #Guardar datos
        return redirect('autos') #Redireccionar datos
    return render(request, 'autos/crear.html', {'formulario': formulario})

def editar_auto(request, id):
    auto = Auto.objects.get(id=id)
    formulario = AutoForm(request.POST or None, request.FILES or None, instance=auto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('autos')
        
    return render(request, 'autos/editar.html', {'formulario': formulario})

def eliminar_auto(request, id):
    auto = Auto.objects.get (id=id)
    auto.delete()
    return render(request, 'autos')


#CRUD USUARIO

def crear_usuario(request):
    #Request FILE recepciona archivos
    formulario_usuario = UsuarioForm(request.POST or None, request.FILES or None)
    if formulario_usuario.is_valid(): #Recepcionar datos
        formulario_usuario.save() #Guardar datos
        return redirect('usuarios') #Redireccionar datos
    return render(request, 'usuarios/crear_usuario.html', {'formulario': formulario_usuario})
    
def editar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    formulario_usuario = UsuarioForm(request.POST or None, request.FILES or None, instance=usuario)
    if formulario_usuario.is_valid() and request.POST:
        formulario_usuario.save()
        return redirect('usuarios')
        
    return render(request, 'usuarios/editar_usuario.html', {'formulario': formulario_usuario})

def eliminar_usuario(request, id):
    usuario = Usuario.objects.get (id=id)
    usuario.delete()
    return render(request, 'usuarios')

#CRUD EMPLEADO

def crear_empleado(request):
    #Request FILE recepciona archivos
    formulario_empleado = EmpleadoForm(request.POST or None, request.FILES or None)
    if formulario_empleado.is_valid(): #Recepcionar datos
        formulario_empleado.save() #Guardar datos
        return redirect('empleados') #Redireccionar datos
    return render(request, 'empleados/crear_empleado.html', {'formulario': formulario_empleado})
    
def editar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    formulario_empleado = EmpleadoForm(request.POST or None, request.FILES or None, instance=empleado)
    if formulario_empleado.is_valid() and request.POST:
        formulario_empleado.save()
        return redirect('empleados')
        
    return render(request, 'empleados/editar_empleado.html', {'formulario': formulario_empleado})

def eliminar_empleado(request, id):
    empleado = Empleado.objects.get (id=id)
    empleado.delete()
    return render(request, 'empleados')

# def registro(request):
#     data = {
#         'form': CustomUserCreationForm()
#     }
    
#     if request.method=='POST':
#         formulario = CustomUserCreationForm(data=request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
#             login(request,user)
#             messages.success(request, "Te has registrado correctamente")
#             return redirect(to="inicio")
#         data['form'] = formulario

    
#     return render(request, 'registration/registro.html', data)


def registro(request):
    data = {
        'form': UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["Email"], password=formulario.cleaned_data["Contrasena"])
            if user is not None:
                login(request, user)
                messages.success(request, "Te has registrado correctamente")
                return redirect(to="inicio")
            else:
                messages.error(request, "La autenticación falló. Verifica tus credenciales e intenta de nuevo.")
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)
