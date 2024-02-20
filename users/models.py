from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    phone_number = models.CharField(max_length=10, blank=True, null=True, verbose_name="Номер телефона")
    favorites_id = models.PositiveIntegerField(default=0, verbose_name='Артикул товара')
    favorites_name = models.CharField(max_length=150, unique=True, verbose_name='Название товара')

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

