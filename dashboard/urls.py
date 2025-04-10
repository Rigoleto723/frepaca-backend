from django.urls import path
from .views import obtenerMetricas

urlpatterns = [
    path('metricas/', obtenerMetricas, name='dashboard-metricas'),
]
