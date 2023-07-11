from rest_framework import serializers
from products.models import WarehouseModel


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseModel
        fields = (
            'id', 'name', 'phone', 'adress', 'created', 'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)
