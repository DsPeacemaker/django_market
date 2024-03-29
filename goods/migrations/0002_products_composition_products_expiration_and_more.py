# Generated by Django 4.2.7 on 2024-02-12 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='composition',
            field=models.TextField(blank=True, null=True, verbose_name='Состав'),
        ),
        migrations.AddField(
            model_name='products',
            name='expiration',
            field=models.IntegerField(blank=True, null=True, verbose_name='Срок годности'),
        ),
        migrations.AddField(
            model_name='products',
            name='temperature',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Температура хранения'),
        ),
    ]
