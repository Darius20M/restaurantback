from rest_framework.viewsets import ModelViewSet

from products.models import WarehouseModel
from products.serializer import WarehouseSerializer


class WarehouseViewSet(ModelViewSet):
    serializer_class = WarehouseSerializer
    queryset = WarehouseModel.objects.all()