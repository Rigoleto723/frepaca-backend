from rest_framework import viewsets
from .models import Pago
from .serializers import PagoSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]
