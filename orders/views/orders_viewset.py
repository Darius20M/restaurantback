from rest_framework.viewsets import ModelViewSet

from orders.models import OrdersModel
from orders.serializer.order_serializer import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = OrdersModel.objects.all()