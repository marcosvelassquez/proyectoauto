from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Auto
from .forms import AutoForm
# Create your views here.

def usuarios(request):
    return render(request, 'paginas/usuarios.html')
def empleados(request):
    return render(request, 'paginas/empleados.html')
def autos(request):
    autos = Auto.objects.all()
    return render(request, 'autos/index.html', {'autos': autos})



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
    

