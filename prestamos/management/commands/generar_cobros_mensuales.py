from django.core.management.base import BaseCommand
from django.utils import timezone
from prestamos.models import Prestamo
from cobros.models import Cobro
from datetime import timedelta
from dateutil.relativedelta import relativedelta

class Command(BaseCommand):
    help = 'Genera cobros mensuales para préstamos activos'

    def handle(self, *args, **kwargs):
        hoy = datetime.now().date()
        prestamosActivos = Prestamo.objects.filter(estado='Activo')

        for prestamo in prestamosActivos:
            # Verificar si ya existe un cobro para este mes
            ultimoCobro = prestamo.cobros.order_by('-fechaVencimiento').first()
            
            if ultimoCobro and ultimoCobro.fechaVencimiento.month == hoy.month:
                continue  # Ya existe un cobro para este mes

            # Calcular el monto de intereses mensual
            montoInteres = (prestamo.saldoActual * prestamo.tasaInteresMensual) / 100
            
            # Calcular la fecha de vencimiento (exactamente un mes después del último cobro o de la fecha de inicio)
            fechaBase = ultimoCobro.fechaVencimiento if ultimoCobro else prestamo.fechaInicio
            fechaVencimiento = fechaBase + relativedelta(months=1)
            
            # Verificar si la fecha de vencimiento es hoy o en el futuro
            if fechaVencimiento <= hoy:
                # Crear el nuevo cobro
                Cobro.objects.create(
                    prestamo=prestamo,
                    montoInteres=montoInteres,
                    fechaVencimiento=fechaVencimiento,
                    notas=f"Cobro de intereses mensual - {fechaVencimiento.strftime('%B %Y')}"
                )
                
                self.stdout.write(
                    self.style.SUCCESS(f'Cobro generado para préstamo {prestamo.id} con fecha {fechaVencimiento}')
                ) 