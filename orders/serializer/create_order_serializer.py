from rest_framework import serializers

from orders.serializer import OrderSerializer

class ProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(write_only=True, required=True)
    quantity = serializers.IntegerField(write_only=True, required=True)


class CreateOrderSerializer(serializers.Serializer):
    reservation_id = serializers.IntegerField(write_only=True, required=True)
    customer_first_name = serializers.CharField(max_length=50, required=True)
    customer_last_name = serializers.CharField(max_length=50, required=True)
    place_chair = serializers.CharField(max_length=2, required=True)
    products = ProductSerializer(many=True, required=True)

"""{
  "reservation_id": 35,
  "customer_first_name": "John",
  "customer_last_name": "Doe",
  "place_chair": "A1",
  "products": [
    {"product_id": 2, "quantity": 2},
    {"product_id": 2, "quantity": 3}
  ]
}"""
