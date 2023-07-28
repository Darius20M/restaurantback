from rest_framework import serializers

from accounts.models import ProfileModel


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileModel
        fields = (
            'id','created', 'modified',
        )
        read_only_fields = ('created', 'modified',)

