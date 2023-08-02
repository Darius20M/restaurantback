from django.db import models
from django.utils import timezone


class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    is_enabled = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        db_table = 'pr_productscategory_t'
        app_label = 'products'
        verbose_name = ('Cat Product')
        verbose_name_plural = ('Cat Products')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ProductCategoryModel, self).save(*args, **kwargs)
