from rest_framework.viewsets import ModelViewSet

from products.models import ProductModel
from products.serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()