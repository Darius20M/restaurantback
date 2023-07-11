# Generated by Django 4.2.2 on 2023-07-11 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billings', '0007_invoicemodel_is_individual_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicemodel',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', max_length=20),
        ),
    ]
