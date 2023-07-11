from django.contrib.auth.models import User
from rest_framework import serializers

#from accounts.serializers.profile_serializer import ProfileSerializer


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField(method_name='get_avatar')

    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'avatar',
        )
        read_only_fields = ('email', 'username',)

    def get_avatar(self, user):
        if user.profile.avatar:
            return user.profile.avatar.url
        return None
