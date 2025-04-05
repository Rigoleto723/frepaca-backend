from rest_framework import viewsets
from .models import HistorialLiquidacion
from .serializers import HistorialLiquidacionSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class HistorialLiquidacionViewSet(viewsets.ModelViewSet):
    queryset = HistorialLiquidacion.objects.all()
    serializer_class = HistorialLiquidacionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
