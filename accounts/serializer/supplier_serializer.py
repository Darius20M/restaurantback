from rest_framework import serializers
from accounts.models import SupplierModel


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierModel
        fields = (
            'id', 'first_name', 'last_name', 'phone', 'email', 'created', 'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)
