from rest_framework.viewsets import ModelViewSet

from gar.models import Marca
from gar.serializers import MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer