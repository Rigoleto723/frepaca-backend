from rest_framework import serializers
from .models import Cobro

class CobroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cobro
        fields = '__all__'
