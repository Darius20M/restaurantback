from django.db import models
from djmoney.models.fields import MoneyField
from django.utils import timezone
from accounts.utils.constants import STATUS


class EmployeeModel(models.Model):
    firstName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    position = models.CharField(max_length=50, null=False, blank=False)
    hireDate = models.DateField(default=timezone.now , null=False, blank=False)
    status = models.CharField(max_length=20,choices=STATUS, default=STATUS.hired, null=False, blank=False)
    salary = MoneyField(decimal_places=2, max_digits=12)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        db_table = 'pr_employee_t'
        app_label = 'products'

    def __str__(self):
        return self.firstName

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(EmployeeModel, self).save(*args, **kwargs)
