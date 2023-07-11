from rest_framework import serializers

from accounts.serializer import CustomerSerializer
from reservations.models import ReservationModel
from reservations.models.tables_model import TableModel
from reservations.serializer import TableSerializer


class ReservationSerializer(serializers.ModelSerializer):
    table = TableSerializer(many=False, read_only=True)
    table_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = ReservationModel
        fields = (
            'id', 'full_name','phone','email','checkin', 'table', 'table_id','status', 'created', 'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)


