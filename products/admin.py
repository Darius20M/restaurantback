from django.contrib import admin, messages

from products.models.product_model import ProductModel
from . import models

# Register your models here.
class comboAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','is_enabled','created','descripcion')
    filter_horizontal = ('product',)


class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','supplier','is_enabled','price','stock','status','descripcion')

    def is_stock_low(self, request):
        # Obtener todos los productos activos con stock igual o menor a 20
        products_with_low_stock = ProductModel.objects.filter(is_enabled=True, stock__lte=20)

        if products_with_low_stock:
            # Construir el mensaje de alerta con los productos con stock bajo
            product_names = ', '.join(str(product) for product in products_with_low_stock)
            messages.warning(request, f"Los siguientes productos tienen un stock igual o menor a 20: {product_names}")

    def changelist_view(self, request, extra_context=None):
        self.is_stock_low(request)
        return super().changelist_view(request, extra_context=extra_context)
        
    
    
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

