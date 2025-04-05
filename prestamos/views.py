from rest_framework import viewsets
from .models import Prestamo
from .serializers import PrestamoSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

