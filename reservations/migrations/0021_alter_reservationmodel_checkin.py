# Generated by Django 4.2.2 on 2023-07-28 18:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0020_reservationmodel_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='checkin',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
