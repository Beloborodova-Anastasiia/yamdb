# Generated by Django 2.2.16 on 2022-06-07 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220607_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(default='user', max_length=16, verbose_name='Пользовательская роль'),
        ),
    ]
