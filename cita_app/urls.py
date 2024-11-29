from django.urls import path
from cita_app import views
urlpatterns = [
    path("cita",views.inicio_vistaCitas, name="cita"),
    path("registrarCita/",views.registrarCita,name="registrarCita"),
    path("seleccionarCita/<id_cita>",views.seleccionarCita,name="seleccionarCita"),
    path("editarCita/",views.editarCita,name="editarCita"),
    path("borrarCita/<id_cita>",views.borrarCita,name="borrarCita")
]
