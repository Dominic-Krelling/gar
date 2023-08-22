from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from gar.models import Categoria
from gar.serializer import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]
