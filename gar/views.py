from rest_framework.viewsets import ModelViewSet

from gar.models import Marca, Cor, Categoria, Acessorio, Veiculo, Modelo
from gar.serializers import MarcaSerializer, CorSerializer, CategoriaSerializer, AcessorioSerializer,ModeloDetailSerializer, ModeloSerializer,VeiculoSerializer, VeiculoDetailSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer


class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ModeloDetailSerializer
        return ModeloSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return VeiculoDetailSerializer
        return VeiculoSerializer