from rest_framework.viewsets import ModelViewSet

from orders.models import OrderDetailModel
from orders.serializer import OrderDetailSerializer


class OrderDetailViewSet(ModelViewSet):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetailModel.objects.all()