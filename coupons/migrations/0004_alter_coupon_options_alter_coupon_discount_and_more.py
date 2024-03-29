# Generated by Django 4.2.7 on 2024-02-13 08:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0003_alter_coupon_active_alter_coupon_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={'verbose_name': 'Купон', 'verbose_name_plural': 'Купоны'},
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.IntegerField(help_text='Значения в процентах (от 0 до 100)', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Скидка в %'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_form',
            field=models.DateTimeField(verbose_name='Действует с'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(verbose_name='Действует до'),
        ),
    ]
