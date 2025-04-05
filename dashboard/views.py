from django.db.models import Sum, Count
from django.utils.timezone import now
from rest_framework.decorators import api_view
from rest_framework.response import Response
from prestamos.models import Prestamo
from cobros.models import Cobro
from pagos.models import Pago
from .serializers import DashboardSerializer

@api_view(['GET'])
def obtener_metricas(request):
    fecha_inicio = now().replace(day=1)  # Primer día del mes
    fecha_fin = now()  # Fecha actual

    # Total invertido en préstamos activos
    total_invertido = Prestamo.objects.filter(activo=True).aggregate(Sum('saldo_actual'))['saldo_actual__sum'] or 0

    # Total de cobros pendientes
    total_cobros_pendientes = Cobro.objects.filter(pagado=False).aggregate(Sum('monto_interes'))['monto_interes__sum'] or 0

    # Clientes al día y en mora
    clientes_al_dia = Cobro.objects.filter(pagado=True).values('prestamo__cliente').distinct().count()
    clientes_en_mora = Cobro.objects.filter(pagado=False).values('prestamo__cliente').distinct().count()

    # Rendimiento teórico mensual (cobros generados en el mes)
    rendimiento_teorico_mensual = Cobro.objects.filter(
        fecha_generacion__range=[fecha_inicio, fecha_fin]
    ).aggregate(Sum('monto_interes'))['monto_interes__sum'] or 0

    # Rendimiento real (pagos recibidos en el mes)
    rendimiento_real = Pago.objects.filter(
        fecha_pago__range=[fecha_inicio, fecha_fin], tipo='interes'
    ).aggregate(Sum('monto'))['monto__sum'] or 0

    # Serializar la respuesta
    data = {
        "total_invertido": total_invertido,
        "total_cobros_pendientes": total_cobros_pendientes,
        "clientes_al_dia": clientes_al_dia,
        "clientes_en_mora": clientes_en_mora,
        "rendimiento_teorico_mensual": rendimiento_teorico_mensual,
        "rendimiento_real": rendimiento_real,
    }

    serializer = DashboardSerializer(data)
    return Response(serializer.data)
