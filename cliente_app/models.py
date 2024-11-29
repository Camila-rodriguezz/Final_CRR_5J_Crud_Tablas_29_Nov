from django.db import models

# Create your models here.
class Clientes(models.Model):
    id_cliente=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    fecha_registro=models.DateField()
    comentarios=models.CharField(max_length=200)
    


    def __str__(self):
        return self.nombre