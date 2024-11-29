from django.shortcuts import render,redirect
from .models import Pagos

# Create your views here.
def inicio_vistaPagos(request):
    lospagos=Pagos.objects.all()
    return render(request,"gestionarPago.html",{"mispagos":lospagos})

def registrarPagos(request):
    id_pago=request.POST["txtid_pago"]
    id_cita=request.POST["txtid_cita"]
    monto=request.POST["txtmonto"]
    fecha_pago=request.POST["txtfecha_pago"]
    metodo_pago=request.POST["txtmetodo_pago"]
    estado_pago=request.POST["txtestado_pago"]
    id_cliente=request.POST["txtid_cliente"]
    

    guardarpagos=Pagos.objects.create(
        id_pago=id_pago,id_cita=id_cita,monto=monto,fecha_pago=fecha_pago,metodo_pago=metodo_pago,estado_pago=estado_pago,id_cliente=id_cliente
    ) # GUARDA EL REGISTRO

    return redirect("pago")

def seleccionarPagos(request,id_pago):
    pago=Pagos.objects.get(id_pago=id_pago)
    return render(request,"editarpago.html",{"mispagos":pago})

def editarPagos(request):
    id_pago=request.POST["txtid_pago"]
    id_cita=request.POST["txtid_cita"]
    monto=request.POST["txtmonto"]
    fecha_pago=request.POST["txtfecha_pago"]
    metodo_pago=request.POST["txtmetodo_pago"]
    estado_pago=request.POST["txtestado_pago"]
    id_cliente=request.POST["txtid_cliente"]
    pago=Pagos.objects.get(id_pago=id_pago)
    pago.id_cita=id_cita
    pago.monto=monto
    pago.fecha_pago=fecha_pago
    pago.metodo_pago=metodo_pago
    pago.estado_pago=estado_pago
    pago.id_cliente=id_cliente
    pago.save() # GUARDA EL REGISTRO
    return redirect("pago")

def borrarPagos (request,id_pago):
    pago=Pagos.objects.get(id_pago=id_pago)
    pago.delete() # ELIMINA EL REGISTRO
    return redirect("pago")