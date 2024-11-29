from django.db import models

# Create your models here.
class Pagos(models.Model):
    id_pago=models.CharField(primary_key=True,max_length=6)
    id_cita=models.CharField(max_length=100)
    monto=models.CharField(max_length=100)
    fecha_pago=models.DateField()
    metodo_pago=models.CharField(max_length=100)
    estado_pago=models.CharField(max_length=10)
    id_cliente=models.CharField(max_length=6)
    


    def __str__(self):
        return self.id_pago