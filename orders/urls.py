from django.urls import re_path
from rest_framework.routers import DefaultRouter

from orders.views import OrderViewSet, OrderDetailViewSet, CreateOrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'ordersdetails', OrderDetailViewSet)

urlpatterns = [
    re_path(r'^create_orders/', CreateOrderViewSet.as_view(), name='CreateOrders'),
]
urlpatterns += router.urls
