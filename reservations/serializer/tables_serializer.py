from rest_framework import serializers
from reservations.models import TableModel


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableModel
        fields = (
            'id', 'capacity','name_type', 'status','created', 'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)