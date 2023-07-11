from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from reservations.exceptions import NotAvailableExceptcion
from reservations.handlers import is_verify_table_available
from reservations.models import ReservationModel, TableModel
from reservations.serializer import CancelReservationSerializer


class CancelReservationViewSet(APIView):

    def put(self, request, pk=None, format=None):

        serializer = CancelReservationSerializer(data=request.data)
        if serializer.is_valid():
            reservation_id = serializer.validated_data['reservation_id']

            try:
                reservation = ReservationModel.objects.get(id=reservation_id)
            except ReservationModel.DoesNotExist:
                return Response({"message": "The reservation has not been found"}, status=status.HTTP_404_NOT_FOUND)

            if reservation.status == 'Cancelled':
                return Response({"message": "The reservation has already been canceled"}, status=status.HTTP_400_BAD_REQUEST)

            reservation.status = 'Cancelled'
            reservation.save()

            table = reservation.table
            table.status = 'Available'
            table.save()

            return Response({"message": "Your reservation has been successfully canceled"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
