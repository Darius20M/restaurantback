from django.contrib import admin
from . import models

# Register your models here.
class comboAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','is_enabled','created','descripcion')
    filter_horizontal = ('product',)


class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','supplier','is_enabled','price','stock','status','descripcion')


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display=('name','is_enabled','descripcion','created')

class WarehouseAdmin(admin.ModelAdmin):
    list_display=('name','phone','adress','created')


class WarehouseDetailAdmin(admin.ModelAdmin):
    list_display=('product','warehouse','stock','created')

admin.site.register(models.ComboModel, comboAdmin)
admin.site.register(models.ProductModel, ProductAdmin)
admin.site.register(models.ProductCategoryModel, ProductCategoryAdmin)
admin.site.register(models.WarehouseModel, WarehouseAdmin)
admin.site.register(models.WarehouseDetailModel, WarehouseDetailAdmin)

