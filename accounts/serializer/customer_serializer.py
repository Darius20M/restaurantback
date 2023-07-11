from rest_framework import serializers
from accounts.models import CustomerModel


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = (
            'id', 'first_name', 'last_name', 'phone', 'email', 'created', 'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)
