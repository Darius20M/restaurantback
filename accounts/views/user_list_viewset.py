from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from accounts.serializer import UserListSerializer



class UserListViewSet(ModelViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['GET'])
    def profile(self, request):
        # Obtener el token/key del request, por ejemplo, desde los headers o los parámetros de la URL
        key = request.GET.get('key')

        try:
            # Buscar el usuario asociado al token/key en la base de datos
            user = User.objects.get(auth_token__key=key)
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)