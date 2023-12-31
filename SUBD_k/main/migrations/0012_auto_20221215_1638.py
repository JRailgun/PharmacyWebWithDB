# Generated by Django 3.2.16 on 2022-12-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_med_med_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='logo_creator',
            field=models.ImageField(blank=True, help_text='Выберите изображение', null=True, upload_to='img/', verbose_name='Лого производителя'),
        ),
        migrations.AlterField(
            model_name='med',
            name='med_photo',
            field=models.ImageField(blank=True, help_text='Выберите изображение', null=True, upload_to='img/', verbose_name='Фото лекарства'),
        ),
        migrations.AlterField(
            model_name='user',
            name='logo_company',
            field=models.ImageField(blank=True, help_text='Выберите изображение', null=True, upload_to='img/', verbose_name='Лого компании'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(blank=True, help_text='Выберите изображение', null=True, upload_to='img/', verbose_name='Фото пользователя'),
        ),
    ]
