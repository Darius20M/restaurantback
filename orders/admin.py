from django.contrib import admin
from . import models

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display=('customer',)

class OrderdetailAdmin(admin.ModelAdmin):
    list_display = ('order',)


admin.site.register(models.OrdersModel, OrderAdmin)
admin.site.register(models.OrderDetailModel, OrderdetailAdmin)
