from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from dj_rest_auth.models import TokenModel

from accounts.serializer.delete_user_serializer import DeleteUserSerializer



class DeleteAccountViewSet(APIView):
   
    def post(self, request, format=None):
        serializer = DeleteUserSerializer(data=request.data)
        if serializer.is_valid():

            token_object = TokenModel.objects.get(key = serializer.validated_data['token'])
            user = token_object.user
            if not user.is_active:
                return Response({'message': 'User no existe'}, status=status.HTTP_200_OK)

            user.is_active = False
            user.username = '+-' + user.username
            user.email = '0' + user.email
            user.set_unusable_password()
            user.save()
            return Response({'message': 'User deleted', 'success': True}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

