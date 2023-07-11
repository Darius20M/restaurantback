from rest_framework import serializers
from products.models import WarehouseDetailModel
from .warehouse_serializer import WarehouseSerializer
from .product_serializer import ProductSerializer


class WarehouseDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    product_id = serializers.IntegerField(write_only=True, required=True)
    warehouse = WarehouseSerializer(many=False, read_only=True)
    warehouse_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = WarehouseDetailModel
        fields = (
            'id', 'stock', 'product', 'product_id', 'warehouse', 'warehouse_id', 'created', 'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)
