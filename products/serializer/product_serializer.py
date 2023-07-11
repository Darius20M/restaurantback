from rest_framework import serializers

from accounts.serializer import SupplierSerializer
from products.models import ProductModel
from products.serializer import ProductCategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(many=False, read_only=True)
    category_id = serializers.IntegerField(write_only=True, required=True)
    supplier = SupplierSerializer(many=False, read_only=True)
    supplier_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = ProductModel
        fields = (
            'id', 'name', 'category', 'category_id', 'supplier', 'supplier_id', 'is_enabled',
            'descripcion', 'price', 'stock', 'status', 'created', 'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)
