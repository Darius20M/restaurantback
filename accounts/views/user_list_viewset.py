from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from accounts.serializer.user_list_serializer import UserListSerializer

from reservations.models.reservation_model import ReservationModel
from reservations.serializer.reservation_serializer import ReservationSerializer

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
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        # Serializar el perfil del usuario
        user_serializer = self.get_serializer(user)

        # Obtener las reservaciones del usuario
        reservations = ReservationModel.objects.filter(user=user)

        # Serializar las reservaciones
        reservation_serializer = ReservationSerializer(reservations, many=True)

        # Combinar el perfil del usuario y las reservaciones en una respuesta
        data = {
            'user_profile': user_serializer.data,
            'user_reservations': reservation_serializer.data,
        }

        return Response(data, status=status.HTTP_200_OK)