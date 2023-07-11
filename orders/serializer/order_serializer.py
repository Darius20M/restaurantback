from rest_framework import serializers
from orders.models import OrdersModel
from reservations.serializer import TableSerializer, ReservationSerializer
from accounts.serializer import CustomerSerializer


class OrderSerializer(serializers.ModelSerializer):

    customer = CustomerSerializer(many=False, read_only=True)
    customer_id = serializers.IntegerField(write_only=True, required=True)
    reservation = ReservationSerializer(many=False, read_only=True)
    reservation_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = OrdersModel
        fields = (
            'id', 'order_date', 'place', 'total_amount', 'customer', 'customer_id',
            'reservation', 'reservation_id', 'status', 'created', 'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)
