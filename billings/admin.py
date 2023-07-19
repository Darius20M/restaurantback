from django.contrib import admin
from . import models

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display=('invoice_number',)

class transactionAdmin(admin.ModelAdmin):
    list_display = ('invoice',)


admin.site.register(models.InvoiceModel, InvoiceAdmin)
admin.site.register(models.TransactionModel, transactionAdmin)