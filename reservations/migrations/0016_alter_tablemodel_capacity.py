# Generated by Django 4.2.2 on 2023-07-19 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0015_remove_reservationmodel_email_reservationmodel_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablemodel',
            name='capacity',
            field=models.IntegerField(choices=[(1, 'one'), (2, 'two'), (4, 'four'), (6, 'six'), (8, 'eight')], default=4),
        ),
    ]