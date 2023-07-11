from django.db import models
from django.db import models
from djmoney.models.fields import MoneyField
from django.utils import timezone


class ComboModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    product = models.ManyToManyField('products.ProductModel')
    is_enabled = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    price = MoneyField(default=0.0,decimal_places=0, max_digits=12)
    stock = models.IntegerField(default=0, blank=False, null=False)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        db_table = 'pr_combos_t'
        app_label = 'products'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ComboModel, self).save(*args, **kwargs)
