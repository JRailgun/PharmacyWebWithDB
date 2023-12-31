# Generated by Django 3.2.16 on 2022-12-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_roles_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mail',
        ),
        migrations.AlterField(
            model_name='user',
            name='date_birth',
            field=models.DateField(blank=True, help_text='Введите дату рождения', null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.BigIntegerField(blank=True, help_text='Введите номер телефона', null=True, verbose_name='Номер телефона'),
        ),
    ]
