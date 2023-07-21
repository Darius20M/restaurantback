from django.contrib import admin
from . import models

# Register your models here.
class customerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','phone','email','created')


class employerAdmin(admin.ModelAdmin):
    list_display=('firstName','lastName','salary','position','hireDate','status','created')


class supplierCategoryAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','phone','email','created')


admin.site.register(models.CustomerModel, customerAdmin)
admin.site.register(models.EmployeeModel, employerAdmin)
admin.site.register(models.SupplierModel, supplierCategoryAdmin)
