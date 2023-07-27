# views.py
from django.shortcuts import render
from rest_framework.views import APIView

from billings.models.invoice_model import InvoiceModel


class imprimir_factura(APIView):

    def post(self, request, format=None):

        return 0


"""def imprimir_factura(request, pk):
    # Recuperar la factura a imprimir usando la clave primaria (pk)
    factura = InvoiceModel.objects.get(pk=pk)

    # Crear un contexto con la información que deseas pasar al template
    context = {
        'factura': factura,
        # Otras variables de contexto que desees pasar al template
    }

    # Renderizar el template 'factura_template.html' con el contexto y devolver la respuesta
    return render(request, 'factura_template.html', context)"""
