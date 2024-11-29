from django.shortcuts import render, redirect
from .models import Citas

# Create your views here.
def inicio_vistaCitas(request):
    lascitas=Citas.objects.all()
    return render(request,"gestionarCita.html",{"miscitas":lascitas})

def registrarCita(request):
    id_cita=request.POST["txtid_cita"]
    fecha_cita=request.POST["txtfecha_cita"]
    hora_cita=request.POST["txthora_cita"]
    id_cliente=request.POST["txtid_cliente"]
    id_empleado=request.POST["txtid_empleado"]
    servicio=request.POST["txtservicio"]
    estado=request.POST["txtestado"]
    

    guardarcitas=Citas.objects.create(
        id_cita=id_cita,fecha_cita=fecha_cita,hora_cita=hora_cita,id_cliente=id_cliente,id_empleado=id_empleado,servicio=servicio,estado=estado
    ) # GUARDA EL REGISTRO

    return redirect("cita")

def seleccionarCita(request,id_cita):
    cita=Citas.objects.get(id_cita=id_cita)
    return render(request,"editarcita.html",{"miscitas":cita})

def editarCita(request):
    id_cita=request.POST["txtid_cita"]
    fecha_cita=request.POST["txtfecha_cita"]
    hora_cita=request.POST["txthora_cita"]
    id_cliente=request.POST["txtid_cliente"]
    id_empleado=request.POST["txtid_empleado"]
    servicio=request.POST["txtservicio"]
    estado=request.POST["txtestado"]
    cita=Citas.objects.get(id_cita=id_cita)
    cita.fecha_cita=fecha_cita
    cita.hora_cita=hora_cita
    cita.id_cliente=id_cliente
    cita.id_empleado=id_empleado
    cita.servicio=servicio
    cita.estado=estado
    cita.save() # GUARDA EL REGISTRO
    return redirect("cita")

def borrarCita (request,id_cita):
    cita=Citas.objects.get(id_cita=id_cita)
    cita.delete() # ELIMINA EL REGISTRO
    return redirect("cita")