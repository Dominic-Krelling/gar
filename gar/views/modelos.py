from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from gar.models import Marca, Cor, Categoria, Acessorio, Veiculo, Modelo
from gar.serializer import MarcaSerializer , CorSerializer, CategoriaSerializer, AcessorioSerializer,ModeloDetailSerializer, ModeloSerializer,VeiculoSerializer, VeiculoDetailSerializer, VeiculoListSerializer

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ModeloDetailSerializer
        return ModeloSerializer