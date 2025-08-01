from django.db import models
from clientes.models import Cliente

class Prestamo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="prestamos")
    montoInicial = models.DecimalField(max_digits=16, decimal_places=2)
    saldoActual = models.DecimalField(max_digits=16, decimal_places=2)
    tasaInteresMensual = models.DecimalField(max_digits=5, decimal_places=2)
    fechaInicio = models.DateField()
    fechaCierre = models.DateField(null=True, blank=True)
    interesMensualGenerado = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=10, default='Activo')
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaActualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Préstamo {self.id} - Cliente {self.cliente}"
