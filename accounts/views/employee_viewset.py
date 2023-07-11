from rest_framework.viewsets import ModelViewSet

from accounts.models import EmployeeModel
from accounts.serializer import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = EmployeeModel.objects.all()