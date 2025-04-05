from rest_framework import serializers

class DashboardSerializer(serializers.Serializer):
    total_invertido = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_cobros_pendientes = serializers.DecimalField(max_digits=10, decimal_places=2)
    clientes_al_dia = serializers.IntegerField()
    clientes_en_mora = serializers.IntegerField()
    rendimiento_teorico_mensual = serializers.DecimalField(max_digits=10, decimal_places=2)
    rendimiento_real = serializers.DecimalField(max_digits=10, decimal_places=2)
