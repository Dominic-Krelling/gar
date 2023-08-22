from rest_framework.serializers import ModelSerializer

from gar.models import Marca, Cor, Categoria, Acessorio, Veiculo, Modelo



class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"