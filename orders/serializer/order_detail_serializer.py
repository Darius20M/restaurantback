from rest_framework import serializers
from orders.models import OrderDetailModel
from accounts.serializer import CustomerSerializer
from orders.serializer.order_serializer import OrderSerializer
from products.serializer import ProductSerializer


class OrderDetailSerializer(serializers.ModelSerializer):
    order = OrderSerializer(many=False, required=True)
    #order_id = serializers.IntegerField(write_only=True, required=True)
    product = ProductSerializer(many=False, read_only=True)
    #product_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = OrderDetailModel
        fields = (
            'id', 'quantity','order', 'product', 'created', 'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)
