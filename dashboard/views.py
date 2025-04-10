from django.db.models import Sum, Count
from django.utils.timezone import now
from rest_framework.decorators import api_view
from rest_framework.response import Response
from prestamos.models import Prestamo
from cobros.models import Cobro
from pagos.models import Pago
from .serializers import DashboardSerializer
from datetime import datetime, timedelta

@api_view(['GET'])
def obtenerMetricas(request):
    # Total invertido (suma de saldos actuales de préstamos activos)
    total_invertido = Prestamo.objects.filter(estado='Activo').aggregate(total=Sum('saldoActual'))['total'] or 0
    
    # Total de intereses generados (suma de montos de intereses de cobros no pagados)
    total_intereses = Cobro.objects.filter(pagado=False).aggregate(total=Sum('montoInteres'))['total'] or 0
    
    # Total de préstamos activos
    total_prestamos_activos = Prestamo.objects.filter(estado='Activo').count()
    
    # Total de préstamos pagados
    total_prestamos_pagados = Prestamo.objects.filter(estado='Pagado').count()
    
    # Total de cobros pendientes
    total_cobros_pendientes = Cobro.objects.filter(pagado=False).count()
    
    # Total de pagos realizados hoy
    hoy = datetime.now().date()
    total_pagos_hoy = Pago.objects.filter(fechaPago=hoy).count()
    
    # Monto total de pagos realizados hoy
    monto_pagos_hoy = Pago.objects.filter(fechaPago=hoy).aggregate(total=Sum('monto'))['total'] or 0
    
    return Response({
        'totalInvertido': float(total_invertido),
        'totalIntereses': float(total_intereses),
        'totalPrestamosActivos': total_prestamos_activos,
        'totalPrestamosPagados': total_prestamos_pagados,
        'totalCobrosPendientes': total_cobros_pendientes,
        'totalPagosHoy': total_pagos_hoy,
        'montoPagosHoy': float(monto_pagos_hoy)
    })
