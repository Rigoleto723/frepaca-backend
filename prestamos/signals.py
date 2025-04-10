from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Prestamo
from cobros.models import Cobro
from datetime import timedelta
from dateutil.relativedelta import relativedelta

@receiver(post_save, sender=Prestamo)
def generar_primer_cobro(sender, instance, created, **kwargs):
    if created:
        # Calcular el monto de intereses mensual
        monto_interes = (instance.montoInicial * instance.tasaInteresMensual) / 100
        
        # Calcular la fecha de vencimiento (exactamente un mes después, manteniendo el mismo día)
        fecha_vencimiento = instance.fechaInicio + relativedelta(months=1)
        
        # Crear el primer cobro
        Cobro.objects.create(
            prestamo=instance,
            monto_interes=monto_interes,
            fecha_vencimiento=fecha_vencimiento,
            notas=f"Cobro de intereses mensual - {fecha_vencimiento.strftime('%B %Y')}"
        ) 