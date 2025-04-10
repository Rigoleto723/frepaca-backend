from django.db import models
from prestamos.models import Prestamo
from django.db.models.signals import post_save
from django.dispatch import receiver

class Pago(models.Model):
    TIPO_PAGO = [
        ('interes', 'Interés'),
        ('abono_capital', 'Abono a Capital'),
    ]

    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE, related_name="pagos")
    cobro = models.ForeignKey('cobros.Cobro', on_delete=models.SET_NULL, null=True, blank=True, related_name="pagos")
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=20, choices=TIPO_PAGO)
    fechaPago = models.DateTimeField()
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Pago {self.tipo} de {self.monto} en préstamo {self.prestamo.id}"

@receiver(post_save, sender=Pago)
def actualizar_prestamo(sender, instance, created, **kwargs):
    if created:
        prestamo = instance.prestamo
        
        if instance.tipo == 'abono_capital':
            # Actualizar el saldo del préstamo
            prestamo.saldoActual -= instance.monto
            prestamo.save()
            
            # Verificar si el préstamo está completamente pagado
            if prestamo.saldoActual <= 0:
                prestamo.estado = 'Pagado'
                prestamo.fechaCierre = instance.fechaPago.date()
                prestamo.save()
        
        elif instance.tipo == 'interes':
            # Buscar el cobro correspondiente
            from cobros.models import Cobro
            cobro = Cobro.objects.filter(
                prestamo=prestamo,
                fechaVencimiento__month=instance.fechaPago.month,
                fechaVencimiento__year=instance.fechaPago.year,
                pagado=False
            ).first()
            
            if cobro:
                cobro.actualizar_estado_pago(instance)
                instance.cobro = cobro
                instance.save()
