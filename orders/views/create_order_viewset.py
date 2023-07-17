from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError


from accounts.models import CustomerModel
from orders.handlers.valid_stock_product import valid_stock_product
from orders.models import OrdersModel, OrderDetailModel
from orders.serializer import OrderDetailSerializer
from orders.serializer import CreateOrderSerializer
from orders.serializer.order_serializer import OrderSerializer
from products.models import ProductModel
from reservations.models import ReservationModel
from django.shortcuts import get_object_or_404



def get_customer(first_name, last_name):
    try:
        customer = CustomerModel.objects.get(first_name=first_name, last_name=last_name)
    except CustomerModel.DoesNotExist:
        customer = CustomerModel.objects.create(first_name=first_name, last_name=last_name)
    return customer


def get_or_create_order(customer_object, reservation_object, place_chair):
    try:

        order_header = OrdersModel.objects.get(customer=customer_object, reservation=reservation_object, place=place_chair)
        return order_header
    except  OrdersModel.DoesNotExist:

        if OrdersModel.objects.filter(place=place_chair).exists():
            raise ValidationError('Ya existe una orden con el lugar')

        order_header = OrdersModel.objects.create(customer=customer_object, reservation=reservation_object, place=place_chair)
        return order_header



class CreateOrderViewSet(APIView):

    def post(self, request, format=None):
        order_serializer = CreateOrderSerializer(data=request.data)

        if order_serializer.is_valid():

            reservation_object = ReservationModel.objects.get(id=order_serializer.validated_data['reservation_id'])

            customer_object = get_customer(order_serializer.validated_data['customer_first_name'],
                                           order_serializer.validated_data['customer_last_name'])

            # aquui poner algo para validar si ya existe una cabecera
            """existing_order = OrdersModel.objects.filter(place=order_serializer.validated_data['place_chair']).exists()
            if existing_order:
                return Response({'error': 'Ya existe una orden con el lugar'},
                                status=status.HTTP_400_BAD_REQUEST)"""

            order_header = get_or_create_order(customer_object, reservation_object, order_serializer.validated_data['place_chair'])

            order_details = []  # Lista para almacenar los objetos OrderDetailModel
            for product_data in order_serializer.validated_data['products']:
                product_id = product_data['product_id']
                quantity = product_data['quantity']

                product_object = valid_stock_product(product_id, quantity)

                order_detail = OrderDetailModel(
                    order=order_header,
                    product=product_object,
                    quantity=quantity
                )
                order_details.append(order_detail)

            OrderDetailModel.objects.bulk_create(order_details)

            return Response(order_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
