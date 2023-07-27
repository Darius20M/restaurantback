from django.db import models
from django.utils import timezone


class SupplierModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        db_table = 'acc_supplier_t'
        app_label = 'accounts'
        verbose_name = ('Cuenta')
        verbose_name_plural = ('Cuentas')

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(SupplierModel, self).save(*args, **kwargs)
