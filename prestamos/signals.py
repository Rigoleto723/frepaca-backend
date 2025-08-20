from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Prestamo
from cobros.models import Cobro
from datetime import timedelta
from dateutil.relativedelta import relativedelta


@receiver(post_save, sender=Prestamo)
def crear_cobro_inicial_intereses(sender, instance, created, **kwargs):
    """
    Si el préstamo se crea con intereses pendientes iniciales,
    se genera un cobro especial en la fecha de inicio.
    """
    if created and instance.interesesPendientesIniciales > 0:
        Cobro.objects.create(
            prestamo=instance,
            montoInteres=instance.interesesPendientesIniciales,
            fechaGeneracion=instance.fechaInicio,
            fechaVencimiento=instance.fechaInicio,  # opcional: podrías poner fechaInicio + 1 mes
            pagado=False,
            notas="Intereses pendientes acumulados antes de registrar el préstamo"
        )

@receiver(post_save, sender=Prestamo)
def generar_cobros_historicos(sender, instance, created, **kwargs):
    if created:
        hoy = timezone.now().date()
        # El primer cobro debe ser un mes después de la fecha de inicio
        fecha_actual = instance.fechaInicio + relativedelta(months=1)
        
        # Generar cobros hasta el mes actual
        while fecha_actual <= hoy:
            # Verificar si ya existe un cobro para este mes
            cobro_existente = Cobro.objects.filter(
                prestamo=instance,
                fechaVencimiento__year=fecha_actual.year,
                fechaVencimiento__month=fecha_actual.month
            ).first()
            
            if not cobro_existente:
                # Calcular el monto de intereses mensual
                montoInteres = (instance.saldoActual * instance.tasaInteresMensual) / 100
                
                # Crear el cobro
                Cobro.objects.create(
                    prestamo=instance,
                    montoInteres=montoInteres,
                    fechaGeneracion=instance.fechaInicio,  # La fecha de generación es cuando se otorgó el préstamo
                    fechaVencimiento=fecha_actual,  # La fecha de vencimiento es un mes después
                    notas=f"Cobro de intereses mensual - {fecha_actual.strftime('%B %Y')}"
                )
            
            # Avanzar al siguiente mes
            fecha_actual = fecha_actual + relativedelta(months=1) 