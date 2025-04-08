from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'  # Incluir todos los campos
        read_only_fields = ('fechaCreacion', 'fechaActualizacion')  
