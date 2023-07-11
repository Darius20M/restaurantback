from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from reservations.exceptions import NotAvailableExceptcion
from reservations.handlers import is_verify_table_available
from reservations.models import ReservationModel, TableModel
from reservations.serializer import CreateReservationSerializer


class CreateReservationViewSet(APIView):


    def post(self, request, pk=None, format=None):

        serializer = CreateReservationSerializer(data=request.data)
        if serializer.is_valid():
            if is_verify_table_available(serializer.validated_data['table_id']):
                return NotAvailableExceptcion()

            table_object = TableModel.objects.get(id = serializer.validated_data['table_id'])
            table_object.status = 'Reserved'
            table_object.save()


            reservation = ReservationModel.objects.create(
                table=table_object,
                status='Pending',
                ** serializer.validated_data
            )

            return Response({"message": "Reserva creada exitosamente"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
