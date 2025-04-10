from rest_framework import viewsets
from .models import Cobro
from .serializers import CobroSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

class CobroViewSet(viewsets.ModelViewSet):
    queryset = Cobro.objects.all()
    serializer_class = CobroSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    @action(detail=False, methods=['get'], url_path='prestamo/(?P<prestamo_id>\d+)')
    def by_prestamo(self, request, prestamo_id=None):
        cobros = Cobro.objects.filter(prestamo_id=prestamo_id)
        serializer = self.get_serializer(cobros, many=True)
        return Response(serializer.data)