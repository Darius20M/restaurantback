from django.contrib import admin
from . import models

# Register your models here.
class tablaAdmin(admin.ModelAdmin):
    list_display=('name_type',)

class reservaAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(models.TableModel, tablaAdmin)
admin.site.register(models.ReservationModel, reservaAdmin)
