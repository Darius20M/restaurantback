from products.models import ProductModel
from rest_framework import status
from rest_framework.response import Response


def valid_stock_product(product_id, quantity ) -> ProductModel:

    try:
        product = ProductModel.objects.get(id = product_id)

        if product.stock <= quantity:
            raise ValueError("No hay stock suficiente")

        product.stock -= quantity
        product.save()

        return product
    except ProductModel.DoesNotExist:
        return Response("The product dosent exist", status=status.HTTP_400_BAD_REQUEST)

