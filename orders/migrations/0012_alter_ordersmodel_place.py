# Generated by Django 4.2.2 on 2023-07-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_alter_ordersmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersmodel',
            name='place',
            field=models.CharField(choices=[('A1', '1'), ('A2', '2'), ('A3', '3'), ('A4', '4'), ('A5', '5'), ('A6', '6'), ('A7', '7'), ('A8', '8')], default='A1'),
        ),
    ]
