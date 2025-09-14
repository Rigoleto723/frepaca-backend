from django.core.management.base import BaseCommand
from prestamos.models import Prestamo
from cobros.models import Cobro

class Command(BaseCommand):
    help = 'Elimina cobros inválidos generados en la misma fecha de inicio del préstamo'

    def handle(self, *args, **kwargs):
        total_eliminados = 0

        prestamos = Prestamo.objects.all()
        for prestamo in prestamos:
            cobros_invalidos = Cobro.objects.filter(
                prestamo=prestamo,
                fechaVencimiento=prestamo.fechaInicio
            )
            cantidad = cobros_invalidos.count()

            if cantidad > 0:
                cobros_invalidos.delete()
                total_eliminados += cantidad
                self.stdout.write(
                    self.style.WARNING(
                        f'Se eliminaron {cantidad} cobro(s) inválido(s) para el préstamo {prestamo.id} (fecha inicio: {prestamo.fechaInicio})'
                    )
                )

        if total_eliminados == 0:
            self.stdout.write(self.style.SUCCESS('No se encontraron cobros inválidos 🎉'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Total de cobros eliminados: {total_eliminados}'))
