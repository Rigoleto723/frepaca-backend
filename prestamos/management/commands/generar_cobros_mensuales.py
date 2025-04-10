from django.core.management.base import BaseCommand
from django.utils import timezone
from prestamos.models import Prestamo
from cobros.models import Cobro
from datetime import timedelta
from dateutil.relativedelta import relativedelta

class Command(BaseCommand):
    help = 'Genera cobros mensuales para préstamos activos'

    def handle(self, *args, **kwargs):
        hoy = timezone.now().date()
        prestamos_activos = Prestamo.objects.filter(estado='Activo')

        for prestamo in prestamos_activos:
            # Verificar si ya existe un cobro para este mes
            ultimo_cobro = prestamo.cobros.order_by('-fecha_vencimiento').first()
            
            if ultimo_cobro and ultimo_cobro.fecha_vencimiento.month == hoy.month:
                continue  # Ya existe un cobro para este mes

            # Calcular el monto de intereses mensual
            monto_interes = (prestamo.saldoActual * prestamo.tasaInteresMensual) / 100
            
            # Calcular la fecha de vencimiento (exactamente un mes después del último cobro o de la fecha de inicio)
            fecha_base = ultimo_cobro.fecha_vencimiento if ultimo_cobro else prestamo.fechaInicio
            fecha_vencimiento = fecha_base + relativedelta(months=1)
            
            # Verificar si la fecha de vencimiento es hoy o en el futuro
            if fecha_vencimiento <= hoy:
                # Crear el nuevo cobro
                Cobro.objects.create(
                    prestamo=prestamo,
                    monto_interes=monto_interes,
                    fecha_vencimiento=fecha_vencimiento,
                    notas=f"Cobro de intereses mensual - {fecha_vencimiento.strftime('%B %Y')}"
                )
                
                self.stdout.write(
                    self.style.SUCCESS(f'Cobro generado para préstamo {prestamo.id} con fecha {fecha_vencimiento}')
                ) 