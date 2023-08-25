from rest_framework.serializers import ModelSerializer, SlugRelatedField

from gar.models import Veiculo
from uploader.models import Image
from uploader.serializers import ImageSerializer

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
        foto_attachment_key = SlugRelatedField (
            source = "foto",
            queryset = Image.objects.all(),
            slug_field = "attachment_key",
            required = False,
            write_only = True
        )
        foto = ImageSerializer(required = False, read_only = True)


class VeiculoDetailSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 2
        foto = ImageSerializer(required = False)
        


class VeiculoListSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ["id", "modelo", "preco"]
