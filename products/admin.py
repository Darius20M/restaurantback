from django.contrib import admin
from . import models

# Register your models here.
class comboAdmin(admin.ModelAdmin):
    list_display=('name',)
    filter_horizontal = ('product',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name',)


class WarehouseDetailAdmin(admin.ModelAdmin):
    list_display = ('product',)

admin.site.register(models.ComboModel, comboAdmin)
admin.site.register(models.ProductModel, ProductAdmin)
admin.site.register(models.ProductCategoryModel, ProductCategoryAdmin)
admin.site.register(models.WarehouseModel, WarehouseAdmin)
admin.site.register(models.WarehouseDetailModel, WarehouseDetailAdmin)

