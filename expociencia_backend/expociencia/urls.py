from rest_framework.routers import DefaultRouter
from expociencia.api.usuario_api import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')

urlpatterns = router.urls
