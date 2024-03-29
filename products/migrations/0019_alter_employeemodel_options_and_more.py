# Generated by Django 4.2.2 on 2023-08-02 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_remove_productmodel_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeemodel',
            options={'verbose_name': 'Employee', 'verbose_name_plural': 'Employees'},
        ),
        migrations.AlterModelOptions(
            name='productcategorymodel',
            options={'verbose_name': 'Cat Product', 'verbose_name_plural': 'Cat Products'},
        ),
        migrations.AlterModelOptions(
            name='productmodel',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='warehousedetailmodel',
            options={'verbose_name': 'Cat WareHouse', 'verbose_name_plural': 'Cat WareHouse'},
        ),
        migrations.AlterModelOptions(
            name='warehousemodel',
            options={'verbose_name': 'WareHouse', 'verbose_name_plural': 'WareHouses'},
        ),
    ]
