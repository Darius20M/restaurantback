from rest_framework.viewsets import ModelViewSet

from products.models import WarehouseDetailModel
from products.serializer import WarehouseDetailSerializer


class WarehouseCategoryViewSet(ModelViewSet):
    serializer_class = WarehouseDetailSerializer
    queryset = WarehouseDetailModel.objects.all()