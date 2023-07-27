from django.urls import re_path
from rest_framework.routers import DefaultRouter

from . import views
from billings.views import TransactionViewSet
from billings.views.create_invoice_viewset import CreateInvoiceViewSet
from billings.views.invoice_viewset import InvoiceViewSet
from billings.views.print_invoice_viewset import imprimir_factura

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'invoices', InvoiceViewSet)




urlpatterns = [
    re_path(r'^create_invoice/', CreateInvoiceViewSet.as_view(), name='CreateInvoice'),
    re_path(r'^imprimir_factura/<int:pk>/', imprimir_factura.as_view(), name='imprimir_factura'),

]
urlpatterns += router.urls
