from django.contrib import admin, messages
from django.forms import ValidationError
from rest_framework import status
from rest_framework.response import Response
from reservations.handlers import send_reservation_email
from reservations.models.tables_model import TableModel


from reservations.views.create_reservation_viewset import get_valid_reservation
from . import models

# Register your models here.
class tablaAdmin(admin.ModelAdmin):
    list_display=('code','name_type','capacity','status','created')

    
   

class reservaAdmin(admin.ModelAdmin):
    list_display = ('user','phone','table','checkin','hour','status','created')
    

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'table':
            object_id = request.resolver_match.kwargs.get('object_id')
            if object_id:
                # Cuando se está editando una reserva existente
                kwargs['queryset'] = TableModel.objects.filter(status='reserved')
            else:
                # Cuando se está creando una nueva reserva
                kwargs['queryset'] = TableModel.objects.filter(status='available')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    
    def delete_queryset(self, request, queryset):
            
            for obj in queryset:
                table_object = models.TableModel.objects.get(id=obj.table_id)
                table_object.status = 'available'
                table_object.save()

            queryset.delete()
            self.message_user(request, "Las reservas han sido eliminadas exitosamente", level='SUCCESS')   
   
    def save_model(self, request, obj, form, change):
       
        if get_valid_reservation(user=obj.user):
            self.message_user(request, "No puedes reservar ya existe una reserva pendiente", level='ERROR')
        else:
            table_object = TableModel.objects.get(id = obj.table_id)
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
