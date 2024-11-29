from django.shortcuts import render,redirect
from .models import Mobiliario

# Create your views here.
def inicio_vistaMobiliario(request):
    elmobiliario=Mobiliario.objects.all()
    return render(request,"gestionarMobiliario.html",{"mimobiliario":elmobiliario})

def registrarMobiliario(request):
    id_mobiliario=request.POST["txtid_mobiliario"]
    descripcion=request.POST["txtdescripcion"]
    cantidad=request.POST["txtcantidad"]
    costo=request.POST["txtcosto"]
    fecha_compra=request.POST["txtfecha_compra"]
    estado=request.POST["txtestado"]
    id_sucursales=request.POST["txtsucursales"]
    

    guardarmobiliario=Mobiliario.objects.create(
        id_mobiliario=id_mobiliario,descripcion=descripcion,cantidad=cantidad,costo=costo,fecha_compra=fecha_compra,estado=estado,id_sucursales=id_sucursales
    ) # GUARDA EL REGISTRO

    return redirect("mobiliario")

def seleccionarMobiliario(request,id_mobiliario):
    mobiliario=Mobiliario.objects.get(id_mobiliario=id_mobiliario)
    return render(request,"editarmobiliario.html",{"mimobiliario":mobiliario})

def editarMobiliario(request):
    id_mobiliario=request.POST["txtid_mobiliario"]
    descripcion=request.POST["txtdescripcion"]
    cantidad=request.POST["txtcantidad"]
    costo=request.POST["txtcosto"]
    fecha_compra=request.POST["txtfecha_compra"]
    estado=request.POST["txtestado"]
    id_sucursales=request.POST["txtsucursales"]
    mobiliario=Mobiliario.objects.get(id_mobiliario=id_mobiliario)
    mobiliario.descripcion=descripcion
    mobiliario.cantidad=cantidad
    mobiliario.costo=costo
    mobiliario.fecha_compra=fecha_compra
    mobiliario.estado=estado
    mobiliario.id_sucursales=id_sucursales
    mobiliario.save() # GUARDA EL REGISTRO
    return redirect("mobiliario")

def borrarMobiliario (request,id_mobiliario):
    mobiliario=Mobiliario.objects.get(id_mobiliario=id_mobiliario)
    mobiliario.delete() # ELIMINA EL REGISTRO
    return redirect("mobiliario")