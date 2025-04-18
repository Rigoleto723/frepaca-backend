from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Reporte
from .serializers import ReporteSerializer
from datetime import datetime, date
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from decimal import Decimal

def convert_decimal_to_string(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    elif isinstance(obj, date):
        return obj.isoformat()
    elif isinstance(obj, dict):
        return {k: convert_decimal_to_string(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_decimal_to_string(item) for item in obj]
    return obj

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def activos(self, request):
        start_date = request.query_params.get('startDate')
        end_date = request.query_params.get('endDate')
        
        if not start_date or not end_date:
            return Response({'error': 'Se requieren las fechas de inicio y fin'}, status=400)
        
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Formato de fecha inválido. Use YYYY-MM-DD'}, status=400)
        
        datos = Reporte.generar_reporte_activos(start_date, end_date)
        datos = convert_decimal_to_string(datos)
        reporte = Reporte.objects.create(
            tipo='activos',
            fecha_inicio=start_date,
            fecha_fin=end_date,
            datos=datos
        )
        serializer = self.get_serializer(reporte)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def pendientes(self, request):
        start_date = request.query_params.get('startDate')
        end_date = request.query_params.get('endDate')
        
        if not start_date or not end_date:
            return Response({'error': 'Se requieren las fechas de inicio y fin'}, status=400)
        
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Formato de fecha inválido. Use YYYY-MM-DD'}, status=400)
        
        datos = Reporte.generar_reporte_pendientes(start_date, end_date)
        datos = convert_decimal_to_string(datos)
        reporte = Reporte.objects.create(
            tipo='pendientes',
            fecha_inicio=start_date,
            fecha_fin=end_date,
            datos=datos
        )
        serializer = self.get_serializer(reporte)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def intereses(self, request):
        start_date = request.query_params.get('startDate')
        end_date = request.query_params.get('endDate')
        
        if not start_date or not end_date:
            return Response({'error': 'Se requieren las fechas de inicio y fin'}, status=400)
        
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Formato de fecha inválido. Use YYYY-MM-DD'}, status=400)
        
        datos = Reporte.generar_reporte_intereses(start_date, end_date)
        datos = convert_decimal_to_string(datos)
        reporte = Reporte.objects.create(
            tipo='intereses',
            fecha_inicio=start_date,
            fecha_fin=end_date,
            datos=datos
        )
        serializer = self.get_serializer(reporte)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def pagados(self, request):
        start_date = request.query_params.get('startDate')
        end_date = request.query_params.get('endDate')
        
        if not start_date or not end_date:
            return Response({'error': 'Se requieren las fechas de inicio y fin'}, status=400)
        
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Formato de fecha inválido. Use YYYY-MM-DD'}, status=400)
        
        datos = Reporte.generar_reporte_pagados(start_date, end_date)
        datos = convert_decimal_to_string(datos)
        reporte = Reporte.objects.create(
            tipo='pagados',
            fecha_inicio=start_date,
            fecha_fin=end_date,
            datos=datos
        )
        serializer = self.get_serializer(reporte)
        return Response(serializer.data)