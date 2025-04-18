from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class ClienteViewSet(viewsets.ModelViewSet):
    """
    API para gestionar clientes.
    Soporta listar, crear, actualizar y eliminar clientes.
    """
    queryset = Cliente.objects.all().order_by('-fechaCreacion')  # Ordenar por fecha reciente
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]
