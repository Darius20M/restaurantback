from datetime import datetime
from django.contrib import admin, messages

from billings.forms import TuModeloForm
from billings.models.invoice_model import InvoiceModel
from billings.views.create_invoice_viewset import get_order, get_order_individual
from orders.models.orders_model import OrdersModel
from reservations.models.reservation_model import ReservationModel
from . import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pdfkit
from django.shortcuts import render

def generate_invoice_html(request,obj, list):
    nombre = obj.nombre
    apellido = obj.apellido
    total_amount = obj.total_amount
    detalle_factura = []

    for i in list:
        d = {'producto': i.product.name, 'cantidad': i.quantity, 'precio_unitario': i.product.price}
        detalle_factura.append(d)

    for item in detalle_factura:
        item['total_item'] = item['cantidad'] * item['precio_unitario']

    # Renderizar la plantilla HTML con los datos de la factura
    html_content = render_to_string('invoice_template_.html', {
        'id': obj.id,
        'nombre': nombre,
        'apellido': apellido,
        'total_amount': total_amount,
        'detail_items': detalle_factura,
    })

    return HttpResponse(html_content, content_type='text/html')

def get_table(invoice_number):
    try:
        invoice = InvoiceModel.objects.get(invoice_number=invoice_number)
        order_details_list = []  # Lista para almacenar los detalles de la orden

        # Recorre todas las órdenes asociadas a la factura
        for order in invoice.orders.all():
            # Recorre los detalles de la orden y agrega cada detalle a la lista
            for order_detail in order.orderdetailmodel_set.all():
                order_details_list.append(order_detail)

        return order_details_list

    except InvoiceModel.DoesNotExist:
        return []

    
def print_button(modeladmin, request, queryset):
    
    invoices_content = []

    # Recorremos los objetos seleccionados en el queryset
    for invoice in queryset:
        invoice_number=invoice.invoice_number
        order = get_table(invoice.invoice_number)
        total = order[0].order.calculate_total_amount
        impustos = total * 0.18
        toal_final = total + impustos

        code = order[0].order.reservation.table.code
        place_set = {registro.order.place for registro in order}


        type_ = order[0].order.reservation.table.name_type
        invoice_content = render_to_string('invoice_template.html', {
            'client':place_set,
            'invoice_number': invoice_number,
            'date': datetime.now(),
            'total_amount':invoice.total_amount,
            'order':order,
            'subtotal': total,
            'itbs': impustos,
            'total_final': toal_final,
            'code':code,
            'type':type_
            
        })
        invoices_content.append(invoice_content)

    # Unimos el contenido de todas las facturas seleccionadas en un solo HTML
    combined_html = "\n".join(invoices_content)

    return HttpResponse(combined_html, content_type='text/html')



print_button.short_description = 'Imprimir'

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','invoice_number', 'is_individual', 'total_amount', 'status', 'created')
    form = TuModeloForm
    readonly_fields = ('invoice_number','total_amount','status',)

    
    actions = [print_button]
   
   
    def save_model(self, request, obj, form, change):
        nombre = form.cleaned_data['Nombre']
        apellido = form.cleaned_data['Apellido']
        is_individual = obj.is_individual
        table = form.cleaned_data['table']
        place = form.cleaned_data['place']

    

        if True:
            order_individual=[]
            for i in place:

                order = OrdersModel.objects.filter(reservation__table=table, place=i, status='Pending')
                #place.remove(i)
                if not order.exists():
                    return self.message_user(request, "La orden {i} fue facturada o no existe", level='ERROR')   
                
                order_individual.append(order)

            amount = 0
            data = []

            order_details_list=[]
            for ib in order_individual:
                order_individual_inst = ib.first()
                amount += order_individual_inst.calculate_total_amount

               
                obj.nombre=nombre
                obj.apellido=apellido
                obj.total_amount = amount
                obj.is_individual=is_individual
                obj.save()
                obj.orders.add(*ib)
                obj.save()
        
                order_individual_inst.status = 'Invoiced'
                order_individual_inst.total_amount = order_individual_inst.calculate_total_amount
                order_individual_inst.save()


            if not OrdersModel.objects.filter(reservation__table=table,  status='Pending').exists():
                reservation = ReservationModel.objects.get(table=table, status = 'ongoing')
                reservation.status='completed'
                reservation.save()
                table.status = 'available'
                table.save()
        
            


   

class transactionAdmin(admin.ModelAdmin):
    list_display = ('invoice','payment_method', 'amount','status','created')
    readonly_fields = ('amount','status',)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "invoice":
            kwargs["queryset"] = InvoiceModel.objects.filter(status="pending")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def save_model(self, request, obj, form, change):

        obj.status = 'paid'
        obj.amount = float((float(obj.invoice.total_amount) * 0.18) + float(obj.invoice.total_amount))
        obj.save()

        obj.invoice.status = 'completed'
        obj.invoice.save()
        


admin.site.register(models.InvoiceModel, InvoiceAdmin)
admin.site.register(models.TransactionModel, transactionAdmin)


