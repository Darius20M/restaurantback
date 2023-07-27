from django.db import models
from djmoney.models.fields import MoneyField
from django.utils import timezone

from billings.utils.constants import PAYMENT_MET


class TransactionModel(models.Model):
    invoice = models.ForeignKey('billings.InvoiceModel', on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=30, choices=PAYMENT_MET, default=PAYMENT_MET.cash, null=False)
    amount = models.FloatField(default=0.0)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)
    status = models.CharField(max_length=21)

    class Meta:
        db_table = 'pr_transactions_t'
        app_label = 'billings'
        verbose_name = ('Transacción')
        verbose_name_plural = ('Transacciónes')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(TransactionModel, self).save(*args, **kwargs)
