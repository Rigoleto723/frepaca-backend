from django.db.models import Sum, Count
from django.http import JsonResponse
from prestamos.models import Prestamo
from cobros.models import Cobro
from pagos.models import Pago

def obtenerMetricas(request):
    totalInvertido = Prestamo.objects.filter(activo=True).aggregate(Sum('saldoActual'))['saldoActualSum'] or 0
    totalCobrosPendientes = Cobro.objects.filter(pagado=False).aggregate(Sum('montoInteres'))['montoInteresSum'] or 0
    clientesAlDia = Cobro.objects.filter(pagado=True).values('prestamoCliente').distinct().count()
    clientesEnMora = Cobro.objects.filter(pagado=False).values('prestamoCliente').distinct().count()
    
    data = {
        "totalInvertido": totalInvertido,
        "totalCobrosPendientes": totalCobrosPendientes,
        "clientesAlDia": clientesAlDia,
        "clientesEnMora": clientesEnMora,
    }
    return JsonResponse(data)
