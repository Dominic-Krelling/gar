from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from gar.models import Acessorio
from gar.serializer import AcessorioSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer


