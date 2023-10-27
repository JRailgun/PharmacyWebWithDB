from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()


class AddSupply(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ['shipper_id', 'datetime_supply']
        widgets = {
            'datetime_supply': forms.DateTimeInput(attrs={'class': 'myfield'}),
        }


class AddSale(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['user_id', 'datetime_sale']
        widgets = {
            'datetime_sale': forms.DateTimeInput(attrs={'class': 'myfield'}),
        }


class AddSaleComp(forms.ModelForm):
    class Meta:
        model = Sale_compos
        fields = ['sale_id', 'med_id', 'quantity_sale', 'recept_photo']
        widgets = {
            'quantity_sale': forms.NumberInput(attrs={'class': 'myfield'}),
        }


class AddSupplyComp(forms.ModelForm):
    class Meta:
        model = Supply_compos
        fields = ['supply_id', 'med_id', 'quantity_supply']
        widgets = {
            'quantity_supply': forms.NumberInput(attrs={'class': 'myfield'}),
        }


class AddAdress(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ['country', 'city', 'street', 'num_house', 'num_apart']
        widgets = {
            'country': forms.TextInput(attrs={'class': 'myfield'}),
            'city': forms.TextInput(attrs={'class': 'myfield'}),
            'street': forms.TextInput(attrs={'class': 'myfield'}),
            'num_house': forms.NumberInput(attrs={'class': 'myfield'}),
            'num_apart': forms.NumberInput(attrs={'class': 'myfield'}),
        }


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user