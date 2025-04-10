from rest_framework import serializers
from .models import Reporte
from decimal import Decimal
import json

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = [
            'id',
            'tipo',
            'fecha_inicio',
            'fecha_fin',
            'datos',
            'fecha_creacion',
            'fecha_actualizacion'
        ]
        read_only_fields = ['fecha_creacion', 'fecha_actualizacion']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if 'datos' in data and data['datos']:
            # Convertir valores decimales a strings en los datos
            def convert_decimal(obj):
                if isinstance(obj, Decimal):
                    return str(obj)
                elif isinstance(obj, dict):
                    return {k: convert_decimal(v) for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [convert_decimal(item) for item in obj]
                return obj
            
            data['datos'] = convert_decimal(data['datos'])
        return data