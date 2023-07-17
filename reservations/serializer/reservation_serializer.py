from rest_framework import serializers

from accounts.serializer import CustomerSerializer, UserListSerializer
from reservations.models import ReservationModel
from reservations.models.tables_model import TableModel
from reservations.serializer import TableSerializer


class ReservationSerializer(serializers.ModelSerializer):
    table = TableSerializer(many=False, read_only=True)
    table_id = serializers.IntegerField(write_only=True, required=True)
    user = UserListSerializer(many=False, read_only=True)
    user_id = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = ReservationModel
        fields = (
            'id','checkin','phone', 'table','user','user_id', 'table_id','status', 'created', 'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)


