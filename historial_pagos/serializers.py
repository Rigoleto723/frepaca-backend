from rest_framework import serializers
from .models import HistorialLiquidacion

class HistorialLiquidacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialLiquidacion
        fields = '__all__'