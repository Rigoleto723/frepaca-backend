from rest_framework import routers
from .views import InversionistaViewSet

router = routers.DefaultRouter()
router.register(r'inversionistas', InversionistaViewSet, basename='inversionista')

urlpatterns = router.urls