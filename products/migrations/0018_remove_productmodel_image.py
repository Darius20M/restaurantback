# Generated by Django 4.2.2 on 2023-07-28 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_combomodel_options_alter_employeemodel_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='image',
        ),
    ]