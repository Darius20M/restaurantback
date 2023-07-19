from rest_framework import serializers
from products.models import ComboModel, ProductModel
from .product_serializer import ProductSerializer


class ComboSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)

    product_id = serializers.ListField(child=serializers.IntegerField(), write_only=True, required=True)

    class Meta:
        model = ComboModel
        fields = (
            'id', 'name', 'product', 'product_id', 'is_enabled', 'descripcion', 'price',
            'stock', 'created','modified',
        )
        read_only_fields = ('id', 'created', 'modified',)

    def validate_product_ids(self, value):
        # Verificar que la lista de IDs de productos no esté vacía
        if not value:
            raise serializers.ValidationError("La lista de product_ids no puede estar vacía.")

        # Verificar que los IDs de productos existen en la base de datos
        products = ProductModel.objects.filter(pk__in=value)
        if products.count() != len(value):
            raise serializers.ValidationError("Uno o más product_ids no existen.")

        value_list = []
        for product in value:
            products = ProductModel.objects.get(id=product)
            value_list.append(products)

        return value_list

    def create(self, validated_data):
        product_ids = self.validate_product_ids(validated_data['product_id'])

        combo = ComboModel.objects.create(
            name=validated_data['name'],
            descripcion=validated_data['descripcion'],
            is_enabled=validated_data['is_enabled'],
            stock=validated_data['stock']
        )
        print(product_ids)

        combo.product.set(product_ids)

        return combo