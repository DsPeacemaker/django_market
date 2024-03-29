# Generated by Django 4.2.7 on 2024-02-13 07:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={'ordering': ('code',), 'verbose_name': 'Купон', 'verbose_name_plural': 'Купоны'},
        ),
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=30, unique=True, verbose_name='Пин-код'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Скидка'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_form',
            field=models.DateTimeField(verbose_name='Активен с'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(verbose_name='Активен до'),
        ),
        migrations.AlterModelTable(
            name='coupon',
            table='Coupons',
        ),
    ]
