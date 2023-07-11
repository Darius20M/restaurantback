from rest_framework import serializers
from products.models import ComboModel
from .product_serializer import ProductSerializer


class ComboSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    product_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = ComboModel
        fields = (
            'id', 'name', 'product', 'product_id', 'is_enabled', 'descripcion', 'price',
            'stock', 'created','modified',
        )
        read_only_fields = ('id', 'created', 'modified',)



