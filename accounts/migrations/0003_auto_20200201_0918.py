# Generated by Django 3.0 on 2020-02-01 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_orders_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Deliverd'), ('Pending', 'Pending'), ('Outfordelivery', 'Outfordelivery')], max_length=100),
        ),
    ]
