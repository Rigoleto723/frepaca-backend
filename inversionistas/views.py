from rest_framework import viewsets, permissions
from .models import Inversionista
from .serializers import InversionistaSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class InversionistaViewSet(viewsets.ModelViewSet):
    queryset = Inversionista.objects.all().order_by('-id')
    serializer_class = InversionistaSerializer
    permission_classes = [IsAuthenticated] 