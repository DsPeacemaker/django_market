# Generated by Django 4.2.7 on 2024-02-13 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_alter_coupon_options_alter_coupon_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='active',
            field=models.BooleanField(verbose_name='Активный'),
        ),
        migrations.AlterModelTable(
            name='coupon',
            table='coupons',
        ),
    ]
