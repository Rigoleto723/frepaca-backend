from rest_framework import serializers

class DashboardSerializer(serializers.Serializer):
    totalInvertido = serializers.DecimalField(max_digits=10, decimal_places=2)
    totalCobrosPendientes = serializers.DecimalField(max_digits=10, decimal_places=2)
    clientesAlDia = serializers.IntegerField()
    clientesEnMora = serializers.IntegerField()
    rendimientoTeoricoMensual = serializers.DecimalField(max_digits=10, decimal_places=2)
    rendimientoReal = serializers.DecimalField(max_digits=10, decimal_places=2)
