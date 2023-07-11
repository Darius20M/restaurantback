from rest_framework.viewsets import ModelViewSet

from reservations.models import TableModel
from reservations.serializer import TableSerializer


class TableViewSet(ModelViewSet):
    serializer_class = TableSerializer
    queryset = TableModel.objects.all()
