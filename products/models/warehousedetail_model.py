from django.db import models
from django.db import models
from django.utils import timezone


class WarehouseDetailModel(models.Model):
    product = models.ForeignKey('products.ProductModel', on_delete=models.PROTECT)
    warehouse = models.ForeignKey('products.WarehouseModel', on_delete=models.PROTECT)
    stock = models.IntegerField(default=0, blank=False, null=False)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)


    class Meta:
        db_table = 'acc_warehousedetail_t'
        app_label = 'products'
        verbose_name = ('Cat Almacen')
        verbose_name_plural = ('Cat Almacenes')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(WarehouseDetailModel, self).save(*args, **kwargs)
