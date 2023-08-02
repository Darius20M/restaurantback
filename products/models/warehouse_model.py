from django.db import models
from django.db import models
from django.utils import timezone


class WarehouseModel(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        db_table = 'acc_warehouse_t'
        app_label = 'products'
        verbose_name = ('WareHouse')
        verbose_name_plural = ('WareHouses')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(WarehouseModel, self).save(*args, **kwargs)
