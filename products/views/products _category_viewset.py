from rest_framework.viewsets import ModelViewSet

from products.models import ProductCategoryModel
from products.serializer import ProductCategorySerializer


class ProductCategoryViewSet(ModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategoryModel.objects.all()