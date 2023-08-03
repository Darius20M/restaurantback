# Generated by Django 4.2.2 on 2023-07-30 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customermodel_options_and_more'),
        ('orders', '0014_orderdetailmodel_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersmodel',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customermodel'),
        ),
    ]