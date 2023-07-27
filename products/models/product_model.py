from django.db import models
from djmoney.models.fields import MoneyField
from django.utils import timezone



class ProductModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    category = models.ForeignKey('products.ProductCategoryModel', related_name='products', on_delete=models.CASCADE)
    supplier = models.ForeignKey('accounts.SupplierModel', on_delete=models.PROTECT)
    is_enabled = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    image=models.ImageField(upload_to='product')
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0, blank=False, null=False)
    created = models.DateTimeField(default=timezone.now, editable=False)
    modified = models.DateTimeField(default=timezone.now, editable=False)
    status = models.CharField(max_length=20)


    class Meta:
        db_table = 'pr_products_t'
        app_label = 'products'
        verbose_name = ('Producto')
        verbose_name_plural = ('Productos')


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ProductModel, self).save(*args, **kwargs)
    
