from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, SolicitacaoViewSet

router = DefaultRouter()

router.register("solicitacoes", SolicitacaoViewSet)
router.register("categorias", CategoriaViewSet)

urlpatterns = router.urls