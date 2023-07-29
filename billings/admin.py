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
from django.http import HttpResponse
import pdfkit


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
        type_ = order[0].order.reservation.table.name_type
        invoice_content = render_to_string('invoice_template.html', {
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
    list_display = ('invoice_number', 'is_individual', 'total_amount', 'status', 'created')
    form = TuModeloForm
    readonly_fields = ('invoice_number','total_amount','status',)

    
    actions = [print_button]
   
    def save_model(self, request, obj, form, change):

        is_individual = obj.is_individual
        table = form.cleaned_data['table']
        place = form.cleaned_data['place']

        if is_individual:
            order = OrdersModel.objects.filter(reservation__table=table, place=place, status='Pending')
            order_individual = order

            
            if not order_individual.exists():
                return self.message_user(request, "La orden no existe o fue facturada", level='ERROR')   


            order_individual_inst = order_individual.first()
            amount = order_individual_inst.calculate_total_amount

            obj.total_amount = amount
            obj.is_individual=is_individual
            obj.save()
            obj.orders.set(order_individual)
            
            order_individual_inst.status = 'Invoiced'
            order_individual_inst.total_amount = amount
            order_individual_inst.save()

            if not OrdersModel.objects.filter(reservation__table=table,  status='Pending').exists():
                reservation = ReservationModel.objects.get(table=table, status = 'ongoing')
                reservation.status='completed'
                reservation.save()
                table.status = 'available'
                table.save()
        else:
                
            amount = 0
            order = get_order(table)

            if not order.exists():
                return 0

            for i in order.all():
                i.status = 'Invoiced'
                i.save()
                amount += i.calculate_total_amount

            
            obj.total_amount = amount
            obj.is_individual=is_individual
            obj.save()
            obj.orders.set(order)
            obj.save()

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


