# Generated by Django 4.2.2 on 2023-06-16 08:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_employeemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='hireDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
