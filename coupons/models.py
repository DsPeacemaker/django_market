from enum import unique
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Coupon(models.Model):
    code = models.CharField(max_length=30, unique=True, verbose_name='Пин-код')
    valid_form = models.DateTimeField(verbose_name='Действует с')
    valid_to = models.DateTimeField(verbose_name='Действует до')
    discount = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(100)],
        verbose_name='Скидка в %',
        help_text='Значения в процентах (от 0 до 100)')
    active = models.BooleanField(verbose_name='Активный')

    class Meta:
        db_table = 'coupons'
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'

    def __str__(self) -> str:
        return self.code
    
