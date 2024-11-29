from django.shortcuts import render,redirect
from .models import Clientes

# Create your views here.
def inicio_vistaClientes(request):
    losclientes=Clientes.objects.all()
    return render(request,"gestionarCliente.html",{"misclientes":losclientes})

def registrarClientes(request):
    id_cliente=request.POST["txtid_cliente"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["txttelefono"]
    email=request.POST["txtemail"]
    direccion=request.POST["txtdireccion"]
    fecha_registro=request.POST["txtfecha_registro"]
    comentarios=request.POST["txtcomentarios"]
    

    guardarclientes=Clientes.objects.create(
        id_cliente=id_cliente,nombre=nombre,telefono=telefono,email=email,direccion=direccion,fecha_registro=fecha_registro,comentarios=comentarios
    ) # GUARDA EL REGISTRO

    return redirect("cliente")

def seleccionarClientes(request,id_cliente):
    cliente=Clientes.objects.get(id_cliente=id_cliente)
    return render(request,"editarcliente.html",{"misclientes":cliente})

def editarClientes(request):
    id_cliente=request.POST["txtid_cliente"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["txttelefono"]
    email=request.POST["txtemail"]
    direccion=request.POST["txtdireccion"]
    fecha_registro=request.POST["txtfecha_registro"]
    comentarios=request.POST["txtcomentarios"]
    cliente=Clientes.objects.get(id_cliente=id_cliente)
    cliente.nombre=nombre
    cliente.telefono=telefono
    cliente.email=email
    cliente.direccion=direccion
    cliente.fecha_registro=fecha_registro
    cliente.comentarios=comentarios
    cliente.save() # GUARDA EL REGISTRO
    return redirect("cliente")

def borrarClientes (request,id_cliente):
    cliente=Clientes.objects.get(id_cliente=id_cliente)
    cliente.delete() # ELIMINA EL REGISTRO
    return redirect("cliente")