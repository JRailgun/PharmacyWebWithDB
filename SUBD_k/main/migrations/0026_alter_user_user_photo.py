# Generated by Django 3.2.16 on 2022-12-18 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_user_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_photo',
            field=models.ImageField(blank=True, default='img/placeholder.jpg', help_text='Выберите изображение', null=True, upload_to='img/', verbose_name='Фото пользователя'),
        ),
    ]
