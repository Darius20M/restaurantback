from rest_framework import serializers
from accounts.models import EmployeeModel


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeModel
        fields = (
            'id', 'firstName', 'lastName', 'position', 'hireDate', 'status', 'salary', 'created', 'modified',
        )
        read_only_fields = ('id', 'created', 'modified',)