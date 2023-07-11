from rest_framework import serializers

class CreateInvoiceSerializer(serializers.Serializer):
    is_individual = serializers.BooleanField(required=True)
    place = serializers.CharField(write_only=True, required=True)
    table_id = serializers.IntegerField(write_only=True, required=True)