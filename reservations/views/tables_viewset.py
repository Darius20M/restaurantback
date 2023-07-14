from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from reservations.models import TableModel
from reservations.serializer import TableSerializer


class TableViewSet(ModelViewSet):
    serializer_class = TableSerializer
    queryset = TableModel.objects.all()
    permission_classes = [IsAuthenticated]
