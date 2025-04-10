from rest_framework import serializers
from .models import Cobro

class CobroSerializer(serializers.ModelSerializer):
    notaPago = serializers.SerializerMethodField()

    class Meta:
        model = Cobro
        fields = '__all__'

    def get_notaPago(self, obj):
        # Obtener las notas de todos los pagos asociados al cobro
        pagos = obj.pagos.all()
        return [pago.notas for pago in pagos if pago.notas]
