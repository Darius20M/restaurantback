from django.contrib import admin, messages

from billings.forms import TuModeloForm
from billings.models.invoice_model import InvoiceModel
from billings.views.create_invoice_viewset import get_order, get_order_individual
from orders.models.orders_model import OrdersModel
from reservations.models.reservation_model import ReservationModel
from . import models
from django.urls import reverse
from django.utils.safestring import mark_safe

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'is_individual', 'total_amount', 'status', 'created', 'print_button')
    form = TuModeloForm
    readonly_fields = ('invoice_number','total_amount','status',)

    def print_button(self, request):
        return mark_safe(f'<a href="" target="_blank">Imprimir</a>')
         

    print_button.short_description = 'Imprimir'
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
        obj.amount = obj.invoice.total_amount
        obj.save()

        obj.invoice.status = 'completed'
        obj.invoice.save()
        


admin.site.register(models.InvoiceModel, InvoiceAdmin)
admin.site.register(models.TransactionModel, transactionAdmin)


