from django.db import models
from prestamos.models import Prestamo

class Cobro(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, related_name="cobros")
    montoInteres = models.DecimalField(max_digits=10, decimal_places=2)
    fechaGeneracion = models.DateField()
    fechaVencimiento = models.DateField()
    pagado = models.BooleanField(default=False)
    montoPagado = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fechaPago = models.DateField(null=True, blank=True)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Cobro {self.id} - Préstamo {self.prestamo.id}"

    def actualizar_estado_pago(self, pago):
        if pago.tipo == 'interes':
            self.pagado = True
            self.montoPagado = pago.monto
            self.fechaPago = pago.fechaPago
            self.save()
