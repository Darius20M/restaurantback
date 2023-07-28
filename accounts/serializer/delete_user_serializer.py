from abc import ABC

from rest_framework import serializers


class DeleteUserSerializer(serializers.Serializer):
    token = serializers.CharField()


