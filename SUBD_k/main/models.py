from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import *


class Med_group(models.Model):
    name_group = models.CharField(verbose_name='Название группы лекарств', help_text='Введите название группы', max_length=50)

    def __str__(self):
        return self.name_group

    class Meta:
        verbose_name = 'Группа лекарств'
        verbose_name_plural = 'Группы лекарств'


class Adress(models.Model):
    country = models.CharField(verbose_name='Страна', help_text='Введите название страны', max_length=50)
    city = models.CharField(verbose_name='Город', help_text='Введите название города', max_length=50)
    street = models.CharField(verbose_name='Улица', help_text='Введите название улицы', max_length=50)
    num_house = models.IntegerField(verbose_name='Номер дома', help_text='Введите номер дома', validators=[MinValueValidator(1)])
    num_apart = models.IntegerField(verbose_name='Номер квартиры', help_text='Введите номер квартиры', null=True, blank=True, validators=[MinValueValidator(1)])

    def __str__(self):
        return str(self.country) + ', ' + str(self.city) + ', ' + str(self.street) + ', ' + str(self.num_house)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Shipper(models.Model):
    adress_id = models.ForeignKey('Adress', on_delete=models.CASCADE, verbose_name='Адрес поставщика', help_text='Введите адрес поставщика')
    name_shipper = models.CharField(verbose_name='Название поставщика', help_text='Введите название поставщика', max_length=50)
    INN = models.BigIntegerField(verbose_name='ИНН', help_text='Введите ИНН поставщика', validators=[MinValueValidator(7000000000)])
    KPP = models.BigIntegerField(verbose_name='КПП', help_text='Введите КПП поставщика', validators=[MinValueValidator(100000000)])
    shipper_phone = models.BigIntegerField(verbose_name='Номер телефона', help_text='Введите номер телефона')
    logo_shipper = models.ImageField(upload_to='media/', verbose_name='Лого поставщика', help_text='Выберите изображение', null=True, blank=True)

    def __str__(self):
        return str(self.name_shipper)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Creator(models.Model):
    adress_id = models.ForeignKey('Adress', on_delete=models.CASCADE, verbose_name='Адрес производителя', help_text='Введите адрес производителя')
    name_creator = models.CharField(verbose_name='Название производителя', help_text='Введите название производителя', max_length=50)
    INN = models.BigIntegerField(verbose_name='ИНН', help_text='Введите ИНН производителя', validators=[MinValueValidator(7000000000)])
    KPP = models.BigIntegerField(verbose_name='КПП', help_text='Введите КПП производителя', validators=[MinValueValidator(100000000)])
    creator_phone = models.BigIntegerField(verbose_name='Номер телефона', help_text='Введите номер телефона', validators=[MinValueValidator(89000000000)])
    logo_creator = models.ImageField(upload_to='img/', verbose_name='Лого производителя', help_text='Выберите изображение', null=True, blank=True)

    def __str__(self):
        return str(self.name_creator)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class User(AbstractUser):
    t_name = models.CharField(verbose_name='Отчество', help_text='Введите отчество пользователя', max_length=50, null=True, blank=True)
    name_company = models.CharField(verbose_name='Название компании', help_text='Введите название компании', max_length=50, null=True, blank=True)
    INN = models.BigIntegerField(verbose_name='ИНН', help_text='Введите ИНН', null=True, blank=True, validators=[MinValueValidator(7000000000)])
    KPP = models.BigIntegerField(verbose_name='КПП', help_text='Введите КПП', null=True, blank=True, validators=[MinValueValidator(100000000)])
    adress_id = models.ForeignKey('Adress', on_delete=models.CASCADE, verbose_name='Адрес', help_text='Выберите адрес', null=True, blank=True)
    date_birth = models.DateField(verbose_name='Дата рождения', help_text='Введите дату рождения', null=True, blank=True)
    phone_number = models.BigIntegerField(verbose_name='Номер телефона', help_text='Введите номер телефона', null=True, blank=True, validators=[MinValueValidator(89000000000)])
    user_photo = models.ImageField(upload_to='img/', verbose_name='Фото пользователя', help_text='Выберите изображение', null=True, blank=True, default='img/placeholder.jpg')

    def __str__(self):
        return str(self.last_name) + ' ' + str(self.first_name) + ' ' + str(self.t_name)


class Med(models.Model):
    med_group_id = models.ForeignKey('Med_group', on_delete=models.CASCADE, verbose_name='Группа лекарств', help_text='Выберите группу лекарств')
    creator_id = models.ForeignKey('Creator', on_delete=models.CASCADE, verbose_name='Производитель', help_text='Выберите производителя')
    name_med = models.CharField(verbose_name='Название лекарства', help_text='Введите название лекарства', max_length=50)
    price = models.IntegerField(verbose_name='Цена', help_text='Введите цену', validators=[MinValueValidator(1)])
    quantity = models.IntegerField(verbose_name='Количество, шт.', help_text='Введите количество, шт.', validators=[MinValueValidator(0)])
    med_photo = models.ImageField(upload_to='img/', verbose_name='Фото лекарства', help_text='Выберите изображение', null=True, blank=True)

    def __str__(self):
        return str(self.name_med)

    class Meta:
        verbose_name = 'Лекарство'
        verbose_name_plural = 'Лекарства'


class Sale(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Клиент', help_text='Выберите клиента')
    datetime_sale = models.DateTimeField(verbose_name='Дата и время продажи', help_text='Введите дату и время продажи')

    def __str__(self):
        return str(self.datetime_sale)

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'


class Sale_compos(models.Model):
    sale_id = models.ForeignKey('Sale', on_delete=models.CASCADE, verbose_name='Продажа', help_text='Выберите дату продажи', related_name='compos')
    med_id = models.ForeignKey('Med', on_delete=models.CASCADE, verbose_name='Лекарство', help_text='Выберите лекарство')
    quantity_sale = models.IntegerField(verbose_name='Количество, шт.', help_text='Введите количество, шт.', validators=[MinValueValidator(1)])
    recept_photo = models.ImageField(upload_to='img/', verbose_name='Фото рецепта', help_text='Выберите изображение', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.med_id.quantity = self.med_id.quantity - self.quantity_sale
        self.med_id.save(force_update=True)
        super(Sale_compos, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.med_id.quantity = self.med_id.quantity + self.quantity_sale
        self.med_id.save()
        super(Sale_compos, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.sale_id) + ' ' + str(self.med_id) + ', ' + str(self.quantity_sale) + ' шт.'

    class Meta:
        verbose_name = 'Позиция продажи'
        verbose_name_plural = 'Позиции продаж'


class Supply(models.Model):
    shipper_id = models.ForeignKey('Shipper', on_delete=models.CASCADE, verbose_name='Поставщик', help_text='Выберите поставщика')
    datetime_supply = models.DateTimeField(verbose_name='Дата и время поставки', help_text='Введите дату и время поставки')

    def __str__(self):
        return str(self.datetime_supply)

    def get_absolute_url(self):
        return '/supply'

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'


class Supply_compos(models.Model):
    supply_id = models.ForeignKey('Supply', on_delete=models.CASCADE, verbose_name='Поставка', help_text='Выберите дату поставки')
    med_id = models.ForeignKey('Med', on_delete=models.CASCADE, verbose_name='Лекарство', help_text='Выберите лекарство')
    quantity_supply = models.IntegerField(verbose_name='Количество, шт.', help_text='Введите количество, шт.', validators=[MinValueValidator(1)])

    def __str__(self):
        return str(self.supply_id) + ' ' + str(self.med_id) + ', ' + str(self.quantity_supply) + ' шт.'

    def get_absolute_url(self):
        return '/supply'

    class Meta:
        verbose_name = 'Позиция поставки'
        verbose_name_plural = 'Позиции поставок'

    def save(self, *args, **kwargs):
        self.med_id.quantity = self.med_id.quantity + self.quantity_supply
        self.med_id.save(force_update=True)
        super(Supply_compos, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.med_id.quantity = self.med_id.quantity - self.quantity_supply
        self.med_id.save()
        super(Supply_compos, self).delete(*args, **kwargs)