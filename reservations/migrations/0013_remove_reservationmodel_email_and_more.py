# Generated by Django 4.2.2 on 2023-07-13 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0012_remove_reservationmodel_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservationmodel',
            name='email',
        ),
        migrations.RemoveField(
            model_name='reservationmodel',
            name='phone',
        ),
    ]
