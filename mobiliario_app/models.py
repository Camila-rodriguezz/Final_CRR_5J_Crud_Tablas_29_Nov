from django.db import models

# Create your models here.
class Mobiliario(models.Model):
    id_mobiliario=models.CharField(primary_key=True,max_length=6)
    descripcion=models.CharField(max_length=100)
    cantidad=models.CharField(max_length=100)
    costo=models.CharField(max_length=100)
    fecha_compra=models.DateField()
    estado=models.CharField(max_length=10)
    id_sucursales=models.CharField(max_length=6)
    


    def __str__(self):
        return self.id_mobiliario