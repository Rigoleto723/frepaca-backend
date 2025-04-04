from django.db import models
from prestamos.models import Prestamo

class Pago(models.Model):
    TIPO_PAGO = [
        ('interes', 'Interés'),
        ('abono_capital', 'Abono a Capital'),
    ]

    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, related_name="pagos")
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=20, choices=TIPO_PAGO)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Pago {self.tipo} de {self.monto} en préstamo {self.prestamo.id}"
