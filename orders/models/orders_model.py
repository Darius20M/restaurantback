from django.db import models
from django.db import models
from djmoney.models.fields import MoneyField
from django.utils import timezone


# debo hacerle un cabecera detalle con un post de viewapi
from orders.utils.constants import PLACES, STATUS_ORDER


class OrdersModel(models.Model):
    #customer = models.ForeignKey('accounts.CustomerModel', on_delete=models.CASCADE, null=True, blank=True)
    place = models.CharField(choices=PLACES, default=PLACES.A1)
    reservation = models.ForeignKey('reservations.ReservationModel', on_delete=models.CASCADE)
    order_date = models.DateField(default=timezone.now)
    total_amount = models.FloatField(default=0.00)
    status = models.CharField(max_length=20, choices=STATUS_ORDER, default=STATUS_ORDER.Pending)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        db_table = 'pr_orders_t'
        app_label = 'orders'
        verbose_name = ('Order')
        verbose_name_plural = ('Orders')

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(OrdersModel, self).save(*args, **kwargs)

    @property
    def calculate_total_amount(self) -> float:
        # hacer esto para que sea por cliente
        order_details = self.orderdetailmodel_set.all()
        total = sum(detail.total_price() for detail in order_details)
        return total
