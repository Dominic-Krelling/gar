from rest_framework.serializers import ModelSerializer

from gar.models import Marca, Cor, Categoria, Acessorio, Veiculo, Modelo


class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"
