from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/', include('authentication.urls')),
    path('api/', include('clientes.urls')),
    path('api/', include('prestamos.urls')),
    path('api/', include('pagos.urls')),
    path('api/', include('cobros.urls')),
    path('api/', include('dashboard.urls')),
]
