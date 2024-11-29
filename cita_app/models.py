from django.db import models

# Create your models here.
class Citas(models.Model):
    id_cita=models.CharField(primary_key=True,max_length=6)
    fecha_cita=models.DateField()
    hora_cita=models.CharField(max_length=100)
    id_cliente=models.CharField(max_length=100)
    id_empleado=models.CharField(max_length=100)
    servicio=models.CharField(max_length=100)
    estado=models.CharField(max_length=100)
    
    def __str__(self):
        return self.id_cita