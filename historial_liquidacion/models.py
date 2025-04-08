from django.db import models
from prestamos.models import Prestamo

class HistorialLiquidacion(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    monto_liquidado = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_liquidacion = models.DateTimeField(auto_now_add=True)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Pago {self.monto_liquidado} - Préstamo {self.prestamo.id}"
