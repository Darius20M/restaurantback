from django.contrib import admin, messages

from orders.views.create_order_viewset import get_or_create_order
from . import models


from django.contrib import admin
from .models import OrdersModel, OrderDetailModel


class OrderdetailAdmin(admin.ModelAdmin):
    list_display = ('order','product','quantity','created')


class OrderDetailInline(admin.TabularInline):  # Puedes usar 'admin.StackedInline' si prefieres una vista apilada
    model = OrderDetailModel
    extra = 1  # Número de formularios de detalle en blanco para mostrar al editar

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'place', 'reservation', 'order_date','total_amount','status')
    inlines = [OrderDetailInline]

    def save_model(self, request, obj, form, change):
     
        existing_order = OrdersModel.objects.filter(
            place=obj.place,
            reservation=obj.reservation,
            reservation__status ='ongoing'

        ).exclude(pk=obj.pk).exists()  # Excluimos el objeto actual (pk=obj.pk) para evitar compararlo consigo mismo

        if existing_order:
            messages.error(request, 'Ya existe una orden con el mismo lugar y reserva.')
        else:
            # Guardar el modelo normalmente si no hay conflicto
            super().save_model(request, obj, form, change)

    

    

# Registrar el modelo maestro en el administrador con el administrador personalizado
admin.site.register(OrdersModel, OrderAdmin)
admin.site.register(models.OrderDetailModel, OrderdetailAdmin)

