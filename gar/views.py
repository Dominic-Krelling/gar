from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from gar.models import Marca, Cor, Categoria, Acessorio, Veiculo, Modelo
from gar.serializers import MarcaSerializer, CorSerializer, CategoriaSerializer, AcessorioSerializer,ModeloDetailSerializer, ModeloSerializer,VeiculoSerializer, VeiculoDetailSerializer, VeiculoListSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

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
        if self.action == "list":
            return VeiculoListSerializer
        elif self.action == "retrieve":
            return VeiculoDetailSerializer
        return VeiculoSerializer