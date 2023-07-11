from rest_framework import serializers

from accounts.serializer import CustomerSerializer
from billings.models import TransactionModel
from billings.serializer.invoice_serializer import InvoiceSerializer
from orders.serializer import OrderSerializer


class TransactionSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(many=False, read_only=True)
    invoice_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = TransactionModel
        fields = (
            'id', 'payment_method', 'amount', 'status', 'invoice', 'invoice_id', 'created', 'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)



