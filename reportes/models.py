from django.db import models
from django.utils import timezone
from prestamos.models import Prestamo
from cobros.models import Cobro
from pagos.models import Pago

class Reporte(models.Model):
    TIPO_REPORTE = [
        ('activos', 'Préstamos Activos'),
        ('pendientes', 'Pagos Pendientes'),
        ('intereses', 'Intereses Generados'),
        ('pagados', 'Préstamos Pagados'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_REPORTE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    datos = models.JSONField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['tipo']),
            models.Index(fields=['fecha_inicio', 'fecha_fin']),
        ]
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"Reporte {self.tipo} - {self.fecha_inicio} a {self.fecha_fin}"

    @classmethod
    def generar_reporte_activos(cls, fecha_inicio, fecha_fin):
        prestamos = Prestamo.objects.filter(
            estado='Activo',
            fechaInicio__range=[fecha_inicio, fecha_fin]
        ).values(
            'id',
            'cliente__nombre',
            'montoInicial',
            'saldoActual',
            'tasaInteresMensual',
            'fechaInicio'
        )
        return list(prestamos)

    @classmethod
    def generar_reporte_pendientes(cls, fecha_inicio, fecha_fin):
        cobros = Cobro.objects.filter(
            pagado=False,
            fechaVencimiento__range=[fecha_inicio, fecha_fin]
        ).values(
            'id',
            'prestamo__cliente__nombre',
            'montoInteres',
            'fechaVencimiento',
            'prestamo__id'
        )
        return list(cobros)

    @classmethod
    def generar_reporte_intereses(cls, fecha_inicio, fecha_fin):
        intereses = Cobro.objects.filter(
            fechaGeneracion__range=[fecha_inicio, fecha_fin]
        ).values(
            'prestamo__cliente__nombre',
            'montoInteres',
            'fechaGeneracion',
            'pagado'
        )
        return list(intereses)

    @classmethod
    def generar_reporte_pagados(cls, fecha_inicio, fecha_fin):
        prestamos = Prestamo.objects.filter(
            estado='Pagado',
            fechaCierre__range=[fecha_inicio, fecha_fin]
        ).values(
            'id',
            'cliente__nombre',
            'montoInicial',
            'fechaInicio',
            'fechaCierre'
        )
        return list(prestamos)