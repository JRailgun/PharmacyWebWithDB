# Generated by Django 3.2.16 on 2022-12-19 19:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_user_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='med',
            name='price',
            field=models.IntegerField(help_text='Введите цену', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='med',
            name='quantity',
            field=models.IntegerField(help_text='Введите количество, шт.', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Количество, шт.'),
        ),
    ]
