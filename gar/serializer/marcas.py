from rest_framework.serializers import ModelSerializer

from gar.models import Marca

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"
