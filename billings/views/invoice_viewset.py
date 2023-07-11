from rest_framework.viewsets import ModelViewSet


from billings.models import InvoiceModel
from billings.serializer import InvoiceSerializer


class InvoiceViewSet(ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = InvoiceModel.objects.all()