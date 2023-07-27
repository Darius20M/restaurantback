from django.db import models
from django.utils import timezone
from sequences import get_next_value


from billings.utils.constants import STATUS_CHOICES



class InvoiceModel(models.Model):
    orders = models.ManyToManyField('orders.OrdersModel')
    invoice_number = models.CharField(max_length=200)
    is_individual = models.BooleanField(default=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES.pending)

    class Meta:
        db_table = 'pr_invoice_t'
        app_label = 'billings'

    def __str__(self):
        return self.invoice_number
    

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
            self.invoice_number = "VF{0}{1}".format(
                timezone.now().strftime("%Y%m%d"),
                get_next_value("invoice", initial_value=1000)
            )
        self.modified = timezone.now()
        return super(InvoiceModel, self).save(*args, **kwargs)
