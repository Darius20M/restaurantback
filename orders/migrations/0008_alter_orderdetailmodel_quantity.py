# Generated by Django 4.2.2 on 2023-07-11 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_ordersmodel_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetailmodel',
            name='quantity',
            field=models.FloatField(default=0.0),
        ),
    ]
