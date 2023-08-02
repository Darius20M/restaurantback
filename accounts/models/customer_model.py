from django.db import models
from django.db import models
from django.utils import timezone


class CustomerModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=101)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        db_table = 'acc_customer_t'
        app_label = 'accounts'
        verbose_name = ('Customer')
        verbose_name_plural = ('Customers')

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(CustomerModel, self).save(*args, **kwargs)
