from django.db import models
from django.contrib.auth.models import AbstractUser
from myapp.managers import UserManager

NULLABLE = {'null': True, 'blank': True}


class Organization(models.Model):
    """
    Модель для описания организации
    """
    title = models.CharField(max_length=100, verbose_name='Название организации')
    description = models.TextField(verbose_name='Описание организации', **NULLABLE)
    address = models.CharField(max_length=255, verbose_name='Адрес организации', **NULLABLE)
    postcode = models.CharField(max_length=10,  verbose_name='Почтовый код', **NULLABLE)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.title


class Event(models.Model):
    """
    Модель для описания мероприятия
    """
    title = models.CharField(max_length=100, verbose_name='Название мероприятия')
    description = models.TextField( verbose_name='Описание мероприятия', **NULLABLE)
    organizations = models.ManyToManyField(
        'Organization', verbose_name='Организации участвующие в мероприятии', related_name='organizations'
    )
    image = models.ImageField(upload_to='event_images/', verbose_name='Превью изображение', **NULLABLE)
    date = models.DateTimeField(verbose_name='Дата мероприятия')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title


class User(AbstractUser):
    """
    Модель, описывающая пользователя
    """
    objects = UserManager()

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    organizations = models.ManyToManyField('Organization', related_name='users')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'users'
        ordering = ['id']

    def __str__(self):
        return self.email
