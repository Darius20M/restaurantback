# Generated by Django 4.2.2 on 2023-07-13 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0013_remove_reservationmodel_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationmodel',
            name='email',
            field=models.EmailField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
