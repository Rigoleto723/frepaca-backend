from rest_framework import serializers
from .models import Prestamo
from clientes.serializers import ClienteSerializer
from .models import Cliente

class PrestamoSerializer(serializers.ModelSerializer):
    clienteDetalle = ClienteSerializer(source='cliente', read_only=True)
    fiadorDetalle = ClienteSerializer(source='fiador', read_only=True)

    class Meta:
        model = Prestamo
        fields = '__all__'