from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User
from accounts.serializer import UserListSerializer


class UserListViewSet(ModelViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all()