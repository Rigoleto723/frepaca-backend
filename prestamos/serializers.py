from rest_framework import serializers
from .models import Prestamo
from clientes.serializers import ClienteSerializer

class PrestamoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)

    class Meta:
        model = Prestamo
        fields = '__all__'