from django.core.management.base import BaseCommand
from django.utils import timezone
from prestamos.models import Prestamo
from cobros.models import Cobro
from dateutil.relativedelta import relativedelta
from datetime import datetime

class Command(BaseCommand):
    help = 'Genera cobros históricos para préstamos desde su fecha de creación hasta el presente'

    def handle(self, *args, **kwargs):
        hoy = datetime.now().date()
        prestamos = Prestamo.objects.all()

        for prestamo in prestamos:
            self.stdout.write(f'Procesando préstamo {prestamo.id}...')
            
            # Fecha inicial (fecha de creación del préstamo)
            fecha_actual = prestamo.fechaInicio + relativedelta(months=1)
            
            # Generar cobros hasta el mes actual
            while fecha_actual <= hoy:
                cobro_existente = Cobro.objects.filter(
                    prestamo=prestamo,
                    fechaVencimiento=fecha_actual
                ).first()

                if not cobro_existente:
                    montoInteres = (prestamo.saldoActual * prestamo.tasaInteresMensual) / 100
                    Cobro.objects.create(
                        prestamo=prestamo,
                        montoInteres=montoInteres,
                        fechaGeneracion=hoy,
                        fechaVencimiento=fecha_actual,
                        notas=f"Cobro de intereses mensual - {fecha_actual.strftime('%B %Y')}"
                    )
                    self.stdout.write(
                        self.style.SUCCESS(f'Cobro generado para préstamo {prestamo.id} con fecha {fecha_actual}')
                    )

                fecha_actual += relativedelta(months=1)