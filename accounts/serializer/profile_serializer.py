from rest_framework import serializers

from accounts.models import ProfileModel
from accounts.utils.base_image_field import Base64ImageField


class ProfileSerializer(serializers.ModelSerializer):
    avatar = Base64ImageField(use_url=True, required=False)

    class Meta:
        model = ProfileModel
        fields = (
            'id', 'avatar', 'created', 'modified',
        )
        read_only_fields = ('created', 'modified',)

