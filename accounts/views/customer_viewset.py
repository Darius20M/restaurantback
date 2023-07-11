from rest_framework.viewsets import ModelViewSet

from accounts.models import CustomerModel
from accounts.serializer import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = CustomerModel.objects.all()