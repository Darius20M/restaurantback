# Generated by Django 4.2.2 on 2023-06-16 20:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_warehousedetailmodel2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=49)),
                ('phone', models.CharField(max_length=15)),
                ('adress', models.EmailField(max_length=100)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'db_table': 'acc_warehouse_t',
            },
        ),
        migrations.DeleteModel(
            name='WarehouseDetailModel2',
        ),
    ]
