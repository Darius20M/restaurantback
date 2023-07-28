from abc import ABC

from rest_framework import serializers


class CreateReservationSerializer(serializers.Serializer):
    token = serializers.CharField()

    phone = serializers.CharField(max_length=20)
    #email = serializers.EmailField(max_length=100)
    capacity_table = serializers.IntegerField()
    checkin = serializers.DateTimeField()
