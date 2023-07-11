from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from billings.models import TransactionModel
from billings.serializer.transaction_serializer import TransactionSerializer


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = TransactionModel.objects.all()