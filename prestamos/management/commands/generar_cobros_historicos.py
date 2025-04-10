from django.core.management.base import BaseCommand
from django.utils import timezone
from prestamos.models import Prestamo
from cobros.models import Cobro
from dateutil.relativedelta import relativedelta
from datetime import datetime

class Command(BaseCommand):
    help = 'Genera cobros históricos para préstamos desde su fecha de creación hasta el presente'

    def handle(self, *args, **kwargs):
        hoy = timezone.now().date()
        prestamos = Prestamo.objects.all()

        for prestamo in prestamos:
            self.stdout.write(f'Procesando préstamo {prestamo.id}...')
            
            # Fecha inicial (fecha de creación del préstamo)
            fechaActual = prestamo.fechaInicio
            
            # Generar cobros hasta el mes actual
            while fechaActual <= hoy:
                # Verificar si ya existe un cobro para este mes
                cobro_existente = Cobro.objects.filter(
                    prestamo=prestamo,
                    fechaVencimiento__year=fechaActual.year,
                    fechaVencimiento__month=fechaActual.month
                ).first()
                
                if not cobro_existente:
                    # Calcular el monto de intereses mensual
                    montoInteres = (prestamo.saldoActual * prestamo.tasaInteresMensual) / 100
                    
                    # Crear el cobro
                    Cobro.objects.create(
                        prestamo=prestamo,
                        montoInteres=montoInteres,
                        fechaGeneracion=fechaActual,
                        fechaVencimiento=fechaActual,
                        notas=f"Cobro de intereses mensual - {fechaActual.strftime('%B %Y')}"
                    )
                    
                    self.stdout.write(
                        self.style.SUCCESS(f'Cobro generado para préstamo {prestamo.id} con fecha {fecha_actual}')
                    )
                
                # Avanzar al siguiente mes
                fecha_actual = fecha_actual + relativedelta(months=1) 