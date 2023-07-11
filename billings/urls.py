from django.urls import re_path
from rest_framework.routers import DefaultRouter

from billings.views import TransactionViewSet
from billings.views.create_invoice_viewset import CreateInvoiceViewSet
from billings.views.invoice_viewset import InvoiceViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'invoices', InvoiceViewSet)




urlpatterns = [
    re_path(r'^create_invoice/', CreateInvoiceViewSet.as_view(), name='CreateInvoice'),

]
urlpatterns += router.urls
