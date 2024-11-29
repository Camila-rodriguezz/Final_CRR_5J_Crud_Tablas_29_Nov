from django.urls import path
from mobiliario_app import views
urlpatterns = [
    path("mobiliario",views.inicio_vistaMobiliario, name="mobiliario"),
    path("registrarMobiliario/",views.registrarMobiliario,name="registrarMobiliario"),
    path("seleccionarMobiliario/<id_mobiliario>",views.seleccionarMobiliario,name="seleccionarMobiliario"),
    path("editarMobiliario/",views.editarMobiliario,name="editarMobiliario"),
    path("borrarMobiliario/<id_mobiliario>",views.borrarMobiliario,name="borrarMobiliario")
]