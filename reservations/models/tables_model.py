from django.db import models
from django.utils import timezone
from reservations.utils.constants import QUANTITY, STATUS_TABLES, TYPE_TABLE
from django.contrib.auth.models import User, Group


class TableModel(models.Model):
    name_type = models.CharField(choices=TYPE_TABLE, default=TYPE_TABLE.family, null=False, blank=False)
    code = models.CharField(max_length=3, unique=True)
    assigned_to = models.ManyToManyField(User)
    capacity = models.IntegerField(choices=QUANTITY, default= 4, null=False, blank=False)
    status = models.CharField(max_length=20, choices=STATUS_TABLES, default=STATUS_TABLES.available, null=False, blank=False)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        db_table = 'pr_tables_t'
        app_label = 'reservations'
        verbose_name = ('Table')
        verbose_name_plural = ('Tables')

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(TableModel, self).save(*args, **kwargs)
