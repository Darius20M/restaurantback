# Generated by Django 4.2.2 on 2023-08-01 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_remove_ordersmodel_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetailmodel',
            name='comentario',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]