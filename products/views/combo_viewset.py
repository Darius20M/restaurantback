from rest_framework.viewsets import ModelViewSet

from products.models import ComboModel
from products.serializer import ComboSerializer


class ComboViewSet(ModelViewSet):
    serializer_class = ComboSerializer
    queryset = ComboModel.objects.all()