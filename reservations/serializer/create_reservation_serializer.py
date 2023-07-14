from abc import ABC

from rest_framework import serializers


class CreateReservationSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=50)

    #phone = serializers.CharField(max_length=15)
    #email = serializers.EmailField(max_length=100)
    capacity_table = serializers.IntegerField()
    #checkin = serializers.DateTimeField()
