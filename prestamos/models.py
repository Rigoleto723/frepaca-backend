from django.db import models
from clientes.models import Cliente

class Prestamo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="prestamos")
    monto_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_actual = models.DecimalField(max_digits=10, decimal_places=2)
    tasa_interes_mensual = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateField()
    activo = models.BooleanField(default=True)
    fecha_cierre = models.DateField(null=True, blank=True)
    interes_mensual_generado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Préstamo {self.id} - Cliente {self.cliente}"
