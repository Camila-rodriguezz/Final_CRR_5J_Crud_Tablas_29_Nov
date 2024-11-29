from django.db import models

# Create your models here.
class Sucursales(models.Model):
    id_sucursal=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    horario=models.CharField(max_length=100)
    encargado=models.CharField(max_length=10)
    codigo_postal=models.CharField(max_length=6)    

    def __str__(self):
        return self.nombre