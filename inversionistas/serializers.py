from rest_framework import serializers
from .models import Inversionista

class InversionistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inversionista
        fields = ['id', 'nombre', 'apellido', 'numeroDocumento', 'telefono', 'email', 'activo', 'notas']
        read_only_fields = ['id']