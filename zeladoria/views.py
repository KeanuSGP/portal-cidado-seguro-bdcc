from rest_framework.viewsets import ModelViewSet
from .models import Solicitacao
from .models import Categoria
from .serializers import CategoriaSerializer, SolicitacaoSerializer


class SolicitacaoViewSet(ModelViewSet):
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer