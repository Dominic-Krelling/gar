from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from gar.models import Marca, Cor, Categoria, Acessorio, Veiculo, Modelo
from gar.serializer import MarcaSerializer , CorSerializer, CategoriaSerializer, AcessorioSerializer,ModeloDetailSerializer, ModeloSerializer,VeiculoSerializer, VeiculoDetailSerializer, VeiculoListSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer
