# Generated by Django 5.0.3 on 2024-03-14 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_event_options_alter_organization_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание мероприятия'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес организации'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание организации'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='postcode',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Почтовый код'),
        ),
    ]
