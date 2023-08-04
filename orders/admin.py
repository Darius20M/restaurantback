from django.contrib import admin, messages
from orders.handlers import valid_stock_product

from orders.views.create_order_viewset import get_or_create_order
from products.models.product_model import ProductModel
from reservations.models.reservation_model import ReservationModel
from reservations.models.tables_model import TableModel
from . import models
from django.contrib.auth.models import User, Group


from django.contrib import admin
from .models import OrdersModel, OrderDetailModel


class OrderdetailAdmin(admin.ModelAdmin):
    list_display = ('order','product','quantity','created')

    


class OrderDetailInline(admin.TabularInline):  # Puedes usar 'admin.StackedInline' si prefieres una vista apilada
    model = OrderDetailModel
    extra = 1  # Número de formularios de detalle en blanco para mostrar al editar
    
    def save_model(self, request, obj, form, change):
     
        existing_order = OrdersModel.objects.filter(
            place=obj.place,
            reservation=obj.reservation,
            reservation__status ='ongoing'
        )
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'product':
            # Filtrar las reservaciones con estado 'ongoing'
            kwargs['queryset'] = ProductModel.objects.filter(is_enabled = True, stock__gte=10 ) #stock__gte=10 mayor o que
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','place','get_reservation_code' ,'reservation', 'order_date','total_amount','status')
    readonly_fields = ('order_date','total_amount','status',)
    inlines = [OrderDetailInline]
    
    def get_reservation_code(self, obj):
        return obj.reservation.table.code

    get_reservation_code.short_description = 'Table'
    get_reservation_code.admin_order_field = 'reservation__table__code'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        meseros_group = Group.objects.get(name='Servers')
        if not request.user.is_superuser and meseros_group in request.user.groups.all():            # Filtrar las mesas asignadas al usuario actual
            reservas_asignadas = ReservationModel.objects.filter(table__assigned_to=request.user)
            # Filtrar las órdenes que tienen mesas relacionadas con el usuario actual
            ordenes_filtradas = qs.filter(reservation__in=reservas_asignadas)
            return ordenes_filtradas
        return qs
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'reservation':
            # Filtrar las reservaciones con estado 'ongoing'
            kwargs['queryset'] = ReservationModel.objects.filter(table__assigned_to=request.user,status='ongoing')
    
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        total = OrdersModel.objects.filter(reservation__id=obj.reservation_id).count()
        if obj.reservation.table.capacity <= total:
            messages.error(request, 'Ya alcanzaste el limite de lugares para tu reserva.')
        else:
            
            existing_order = OrdersModel.objects.filter(
                place=obj.place,
                reservation=obj.reservation,
                reservation__status ='ongoing'

            ).exclude(pk=obj.pk).exists()  # Excluimos el objeto actual (pk=obj.pk) para evitar compararlo consigo mismo

            if existing_order:
                messages.error(request, 'Ya existe una orden con el mismo lugar y reserva.')
            else:
                
                obj.save()
                detalle_orden = []
                amount = 0
                for detail in obj.orderdetailmodel_set.all():
                    t = detail.quantity * detail.product.price
                    amount+= t
                obj.total_amount=amount
                obj.save()
                
                super().save_model(request, obj, form, change)

    

    

# Registrar el modelo maestro en el administrador con el administrador personalizado
admin.site.register(OrdersModel, OrderAdmin)
admin.site.register(models.OrderDetailModel, OrderdetailAdmin)

