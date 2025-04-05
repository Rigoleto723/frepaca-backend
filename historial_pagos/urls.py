from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HistorialLiquidacionViewSet

router = DefaultRouter()
router.register(r'historial_liquidacion', HistorialLiquidacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]