# Generated by Django 4.2.2 on 2023-07-27 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_alter_ordersmodel_place'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderdetailmodel',
            options={'verbose_name': 'Det Orden', 'verbose_name_plural': 'Det Ordenes'},
        ),
        migrations.AlterModelOptions(
            name='ordersmodel',
            options={'verbose_name': 'Orden', 'verbose_name_plural': 'Ordenes'},
        ),
    ]
