from django.db import models
from django.db import models
from djmoney.models.fields import MoneyField
from django.utils import timezone


class OrderDetailModel(models.Model):
    order = models.ForeignKey('orders.OrdersModel', on_delete=models.CASCADE)
    product = models.ForeignKey('products.ProductModel', on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    def total_price(self):
        return self.quantity * self.product.price

    def _str_(self):
        return str(self.id)

    class Meta:
        db_table = 'pr_ordersdetail_t'
        app_label = 'orders'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(OrderDetailModel, self).save(*args, **kwargs)
