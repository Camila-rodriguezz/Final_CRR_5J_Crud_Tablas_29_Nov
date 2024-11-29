from django.urls import path
from pago_app import views
urlpatterns = [
    path("pago",views.inicio_vistaPagos, name="pago"),
    path("registrarPagos/",views.registrarPagos,name="registrarPagos"),
    path("seleccionarPagos/<id_pago>",views.seleccionarPagos,name="seleccionarPagos"),
    path("editarPagos/",views.editarPagos,name="editarPagos"),
    path("borrarPagos/<id_pago>",views.borrarPagos,name="borrarPagos")
]