from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from billings.models import InvoiceModel
from billings.serializer import CreateInvoiceSerializer
from orders.models import OrdersModel, OrderDetailModel
from reservations.models import TableModel


def get_table(id_table):
    try:
        table = TableModel.objects.get(id=id_table)
    except TableModel.DoesNotExist:
        return Response("nosir", status=status.HTTP_400_BAD_REQUEST)
    return table


def get_order_individual(table, place):
    try:
        order = OrdersModel.objects.filter(reservation__table=table, place=place, status='Pending')

    except OrdersModel.DoesNotExist:
        return Response("nosir", status=status.HTTP_400_BAD_REQUEST)
    return order


def get_order(table):
    try:
        order = OrdersModel.objects.filter(reservation__table=table, status='Pending')
    except OrdersModel.DoesNotExist:
        return Response("nosir", status=status.HTTP_400_BAD_REQUEST)
    return order


class CreateInvoiceViewSet(APIView):

    def post(self, request, format=None):
        serializer = CreateInvoiceSerializer(data=request.data)

        if serializer.is_valid():
            is_individual = serializer.validated_data['is_individual']
            table = get_table(serializer.validated_data.get('table_id'))
            place = serializer.validated_data.get('place')

            if is_individual:
                order_individual = get_order_individual(table, place)
                if not order_individual.exists():
                    return Response("La order ya fue facturada", status=status.HTTP_400_BAD_REQUEST)

                order_individual_inst = order_individual.first()
                amount = order_individual_inst.calculate_total_amount

                invoice = InvoiceModel.objects.create(  # en un metodo para que no se repitan ordenes
                    #orders=order_individual_inst,
                    is_individual=is_individual,
                    total_amount=amount
                )
                invoice.orders.set(order_individual)

            else:
                amount = 0
                order = get_order(table)

                if not order.exists():
                    return Response("La mesa ya fue facturada", status=status.HTTP_400_BAD_REQUEST)

                for i in order.all():
                    i.status = 'Invoiced'
                    i.save()
                    amount += i.calculate_total_amount

                invoice = InvoiceModel.objects.create(  # en un metodo para que no se repitan ordenes
                    # orders=order_individual_inst,
                    is_individual=is_individual,
                    total_amount=amount
                )
                invoice.orders.set(order)

            response_data = {
                'invoice_id': invoice.id,
                'is_individual': is_individual,
                'total_amount': amount,

            }

            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
