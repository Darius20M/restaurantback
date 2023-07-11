from rest_framework.viewsets import ModelViewSet

from accounts.models import SupplierModel
from accounts.serializer import SupplierSerializer


class SupplierViewSet(ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = SupplierModel.objects.all()