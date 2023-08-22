from rest_framework.serializers import ModelSerializer

from gar.models import Marca, Cor, Categoria, Acessorio, Veiculo, Modelo


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"