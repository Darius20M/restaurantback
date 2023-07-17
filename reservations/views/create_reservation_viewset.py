from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from reservations.exceptions import NotAvailableExceptcion
from reservations.handlers import is_verify_table_available
from reservations.handlers import send_reservation_email
from reservations.models import ReservationModel, TableModel
from reservations.serializer import CreateReservationSerializer

def get_valid_reservation(user):
    try:
        reserva = ReservationModel.objects.filter(user=user, status='Pending').exists()
    except ReservationModel.DoesNotExist:
        return False

    return reserva

def get_table(capacity):
    try:
        table = TableModel.objects.filter(capacity=capacity, status='available').first()
    except TableModel.DoesNotExist:
        return Response({"message": "no existe la mesa"})

    return table


class CreateReservationViewSet(APIView):

    def post(self, request, pk=None, format=None):

        serializer = CreateReservationSerializer(data=request.data)
        if serializer.is_valid():

            if request.user.is_anonymous:
                #return redirect('nombre_de_la_vista_de_registro_o_inicio_de_sesion')
                return Response("logueate", status=status.HTTP_400_BAD_REQUEST)

            if get_valid_reservation(user=request.user):
                return Response("No puedes reservar tienes reserva pendiente", status=status.HTTP_400_BAD_REQUEST)


            table_object = get_table(serializer.validated_data['capacity_table'])
            if table_object is None:
                return Response("Estas mesas no hay disponibles", status=status.HTTP_400_BAD_REQUEST)

            table_object.status = 'Reserved'
            table_object.save()

            reservation = ReservationModel.objects.create(
                user=request.user,
                phone= serializer.validated_data['phone'],
                table=table_object,
                checkin= serializer.validated_data['checkin'],
                status='Pending'
            )
            send_reservation_email(request.user, reservation.id, reservation.checkin.date, reservation.checkin.time,
                                   table_object.name_type, table_object.capacity)

            return Response({"message": "Reserva creada exitosamente"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
