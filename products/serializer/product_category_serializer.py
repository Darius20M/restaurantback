from rest_framework import serializers
from products.models import ProductCategoryModel


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategoryModel
        fields = (
            'id', 'name', 'is_enabled', 'descripcion', 'created', 'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)

