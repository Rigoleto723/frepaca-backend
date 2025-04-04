from django.db.models import Sum, Count
from django.http import JsonResponse
from prestamos.models import Prestamo
from cobros.models import Cobro
from pagos.models import Pago

def obtener_metricas(request):
    total_invertido = Prestamo.objects.filter(activo=True).aggregate(Sum('saldo_actual'))['saldo_actual__sum'] or 0
    total_cobros_pendientes = Cobro.objects.filter(pagado=False).aggregate(Sum('monto_interes'))['monto_interes__sum'] or 0
    clientes_al_dia = Cobro.objects.filter(pagado=True).values('prestamo__cliente').distinct().count()
    clientes_en_mora = Cobro.objects.filter(pagado=False).values('prestamo__cliente').distinct().count()
    
    data = {
        "total_invertido": total_invertido,
        "total_cobros_pendientes": total_cobros_pendientes,
        "clientes_al_dia": clientes_al_dia,
        "clientes_en_mora": clientes_en_mora,
    }
    return JsonResponse(data)
