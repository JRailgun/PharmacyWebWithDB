# Generated by Django 3.2.16 on 2022-12-17 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20221215_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='adress_id',
            field=models.ForeignKey(blank=True, help_text='Выберите адрес', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.adress', verbose_name='Адрес'),
        ),
    ]
