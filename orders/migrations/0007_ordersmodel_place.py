# Generated by Django 4.2.2 on 2023-07-03 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_ordersmodel_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersmodel',
            name='place',
            field=models.CharField(choices=[('A1', '1'), ('A2', '2'), ('A3', '3'), ('A4', '4'), ('A5', '5'), ('A6', '6')], default='A1'),
        ),
    ]
