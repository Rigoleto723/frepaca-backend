from rest_framework import viewsets
from .models import Cobro
from .serializers import CobroSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class CobroViewSet(viewsets.ModelViewSet):
    queryset = Cobro.objects.all()
    serializer_class = CobroSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]