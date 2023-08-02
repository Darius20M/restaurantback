from django.contrib import admin, messages
from django.forms import ValidationError
from rest_framework import status
from rest_framework.response import Response
from reservations.handlers import send_reservation_email
from reservations.models.reservation_model import ReservationModel
from reservations.models.tables_model import TableModel
from django.contrib.auth.models import User


from . import models

def get_table(capacity,checkin,hour,s):
        try:
            table = TableModel.objects.filter(capacity=capacity)
            for i in table:
                reserva = ReservationModel.objects.filter(table=i, checkin=checkin, hour = hour, status= s)
                if not reserva:
                    return i
                    
        except :

            return Response({"message": "no existe la mesa"})
# Register your models here.
class tablaAdmin(admin.ModelAdmin):
    list_display=('id','code','name_type','capacity','status','created')
    search_fields = ['code', 'id','capacity']

    
   

class reservaAdmin(admin.ModelAdmin):
    list_display = ('id','user','phone','table','checkin','hour','status','created')
    autocomplete_fields = ['table']  # Agregar esta línea

    

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            object_id = request.resolver_match.kwargs.get('object_id')
            if object_id:
                # Cuando se está editando una reserva existente
                kwargs['queryset'] = User.objects.filter(is_active=True)
            else:
                # Cuando se está creando una nueva reserva
                kwargs['queryset'] = User.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    
    def delete_queryset(self, request, queryset):
            
            for obj in queryset:
                table_object = models.TableModel.objects.get(id=obj.table_id)
                table_object.status = 'available'
                table_object.save()

            queryset.delete()
            self.message_user(request, "Las reservas han sido eliminadas exitosamente", level='SUCCESS')   
   
    def save_model(self, request, obj, form, change):
       
       
        
            capacity=obj.table.capacity
            checkin=obj.checkin

            hour=obj.hour
            st = obj.status

            table_object = get_table(capacity,checkin,hour, st)
            if table_object is None:
                self.message_user(request, "Las mesa no esta disponible", level='ERROR')
            else:   

                table_object.status = 'reserved'
                table_object.save()
                    
                obj.save()

                send_reservation_email(obj.user, obj.id, obj.checkin, obj.hour,
                                obj.table.name_type, table_object.capacity)
                
                self.message_user(request, "La reserva se ha creado exitosamente", level='SUCCESS')
   
    def change_view(self, request, object_id, form_url='', extra_context=None):
        def formfield_for_foreignkey(self, db_field, request, **kwargs):
            if db_field.name == 'table':
                kwargs['queryset'] = models.TableModel.objects.filter(status='reserved')
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
        
        if request.method == 'POST':

            obj = self.get_object(request, object_id)
            if obj.status == 'cancelled' and obj.table.status != 'available':
                obj.table.status = 'available'
                obj.table.save()
                        
            self.message_user(request, "La reserva se ha modificado exitosamente", level='SUCCESS')
        return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)
        



admin.site.register(models.TableModel, tablaAdmin)
admin.site.register(models.ReservationModel, reservaAdmin)
