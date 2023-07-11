from rest_framework import serializers

from billings.models import InvoiceModel
from orders.serializer import OrderSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    order = OrderSerializer(many=False, read_only=True)
    order_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = InvoiceModel
        fields = (
            'id', 'total_amount', 'invoice_number','is_individual','order', 'order_id','status', 'created', 'modified',
        )
        read_only_fields = ('id', 'created', 'modified','invoice_number',)



