# Generated by Django 4.2.2 on 2023-08-02 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_alter_orderdetailmodel_comentario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderdetailmodel',
            options={'verbose_name': 'Det Order', 'verbose_name_plural': 'Det Orders'},
        ),
        migrations.AlterModelOptions(
            name='ordersmodel',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
    ]