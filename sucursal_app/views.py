from django.shortcuts import render,redirect
from .models import Sucursales

# Create your views here.

def inicio_vistaSucursales(request):
    lassucursales=Sucursales.objects.all()
    return render(request,"gestionarSucursal.html",{"missucursales":lassucursales})

def registrarSucursal(request):
    id_sucursal=request.POST["txtid_sucursal"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    horario=request.POST["txthorario"]
    encargado=request.POST["txtencargado"]
    codigo_postal=request.POST["txtcodigo_postal"]
    

    guardarsucursales=Sucursales.objects.create(
        id_sucursal=id_sucursal,nombre=nombre,direccion=direccion,telefono=telefono,horario=horario,encargado=encargado,codigo_postal=codigo_postal
    ) # GUARDA EL REGISTRO

    return redirect("sucursal")

def seleccionarSucursal(request,id_sucursal):
    sucursal=Sucursales.objects.get(id_sucursal=id_sucursal)
    return render(request,"editarsucursal.html",{"missucursales":sucursal})

def editarSucursal(request):
    id_sucursal=request.POST["txtid_sucursal"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["txttelefono"]
    horario=request.POST["txthorario"]
    encargado=request.POST["txtencargado"]
    codigo_postal=request.POST["txtcodigo_postal"]
    sucursal=Sucursales.objects.get(id_sucursal=id_sucursal)
    sucursal.nombre=nombre
    sucursal.direccion=direccion
    sucursal.telefono=telefono
    sucursal.horario=horario
    sucursal.encargado=encargado
    sucursal.codigo_postal=codigo_postal
    sucursal.save() # GUARDA EL REGISTRO
    return redirect("sucursal")

def borrarSucursal (request,id_sucursal):
    sucursal=Sucursales.objects.get(id_sucursal=id_sucursal)
    sucursal.delete() # ELIMINA EL REGISTRO
    return redirect("sucursal")
