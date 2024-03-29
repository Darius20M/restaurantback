# Generated by Django 4.2.2 on 2023-06-16 20:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_productmodel_supplier_alter_productmodel_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarehouseDetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('stock', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.productmodel')),
            ],
            options={
                'db_table': 'acc_warehousedetail_t',
            },
        ),
    ]
