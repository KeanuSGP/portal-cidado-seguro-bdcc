from rest_framework.routers import DefaultRouter

from user.views import UserViewSet
from zeladoria.views import CategoriaViewSet, SolicitacaoViewSet

router = DefaultRouter()

router.register("usuarios", UserViewSet)
router.register("solicitacoes", SolicitacaoViewSet)
router.register("categorias", CategoriaViewSet)

urlpatterns = router.urls