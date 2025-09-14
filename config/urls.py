from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/', include('clientes.urls')),
    path('api/', include('prestamos.urls')),
    path('api/', include('pagos.urls')),
    path('api/', include('cobros.urls')),
    path('api/', include('dashboard.urls')),
    path('api/', include('reportes.urls')),
    path('api/', include('inversionistas.urls')),
    path('api/docs/', include('docs.urls')),
]
