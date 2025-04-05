from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/clientes/', include('clientes.urls')),
    path('api/prestamos/', include('prestamos.urls')),
    path('api/pagos/', include('pagos.urls')),
    path('api/cobros/', include('cobros.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    path('api/docs/', include('docs.urls')),
]
