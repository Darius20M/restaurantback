from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from dj_rest_auth.models import TokenModel


from reservations.exceptions import NotAvailableExceptcion
from reservations.handlers import is_verify_table_available
from reservations.handlers import send_reservation_email
from reservations.models import ReservationModel, TableModel
from reservations.serializer import CreateReservationSerializer

def get_user(user):
    try:
        token_object = TokenModel.objects.get(key = user)
        user = token_object.user

    except TokenModel.DoesNotExist:
        return False
    return user



def get_valid_reservation(user_):
    try:
        reserva = ReservationModel.objects.filter(user=user_, status='pending')
    except ReservationModel.DoesNotExist:
        return False
#table=table,table__status= "Available", table_id=table.id,checkin=checkin, hour = hour
    return reserva

def get_table(capacity,checkin,hour, user):
    try:
        table = TableModel.objects.filter(capacity=capacity)
        for i in table:
            reserva = ReservationModel.objects.filter(table=i, checkin=checkin, hour = hour)
            if not reserva:
                if not ReservationModel.objects.filter(user=user, checkin=checkin, hour = hour):

                    return i

                   
    except :
        return Response({"message": "no existe la mesa"})
    


class CreateReservationViewSet(APIView):

    def post(self, request, pk=None, format=None):

        serializer = CreateReservationSerializer(data=request.data)
        if serializer.is_valid():

            """if request.user.is_anonymous:
                #return redirect('nombre_de_la_vista_de_registro_o_inicio_de_sesion')
                return Response("logueate", status=status.HTTP_400_BAD_REQUEST)"""
            user = get_user(user=serializer.validated_data['token'])

            if not user:
                return Response("user no existe", status=status.HTTP_400_BAD_REQUEST)

            if  get_valid_reservation(user):
                return Response("No puedes reservar tienes reserva pendiente", status=status.HTTP_400_BAD_REQUEST)

            capacity=serializer.validated_data['capacity_table']
            checkin=serializer.validated_data['checkin']

            hour=serializer.validated_data['hour']

            table_object = get_table(capacity,checkin,hour,user)
            if table_object is None:
                return Response("mesa no disponibles o tienes una reserva para misma hora.", status=status.HTTP_400_BAD_REQUEST)

            table_object.status = 'reserved'
            table_object.save()

            reservation = ReservationModel.objects.create(
                user=user,
                phone= serializer.validated_data['phone'],
                table=table_object,
                checkin= serializer.validated_data['checkin'],
                hour= serializer.validated_data['hour'],
                status='pending'
            )
            send_reservation_email(user, reservation.id, reservation.checkin, reservation.hour,
                                   table_object.name_type, table_object.capacity)

            return Response({"message": "Reserva creada exitosamente"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
