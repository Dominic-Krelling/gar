from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from gar.models import Marca, Cor, Categoria, Acessorio, Veiculo, Modelo
from gar.serializer import MarcaSerializer , CorSerializer, CategoriaSerializer, AcessorioSerializer,ModeloDetailSerializer, ModeloSerializer,VeiculoSerializer, VeiculoDetailSerializer, VeiculoListSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]
