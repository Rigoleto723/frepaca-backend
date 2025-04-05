from django.urls import path
from .views import obtener_metricas

urlpatterns = [
    path('metricas/', obtener_metricas, name='dashboard-metricas'),
]
