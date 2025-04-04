from django.db import models
from prestamos.models import Prestamo

class Cobro(models.Model):
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, related_name="cobros")
    monto_interes = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_generacion = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField()
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"Cobro {self.id} - Préstamo {self.prestamo.id}"
