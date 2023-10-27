from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.contrib.auth import get_user_model
from django.forms.models import modelform_factory
User = get_user_model()


class ModelFormWidgetMixin(object):
    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields, widgets=self.widgets)


def index(request):
    emp = User.objects.filter(is_staff=True)
    return render(request, 'index.html', {'emp': emp})


def admin(request):
    return render(request, 'admin.html')


@login_required(login_url='login')
def catalog1(request):
    med = Med.objects.all()
    return render(request, 'catalog1.html', {'med': med})


def grunmed(request):
    grun = Creator.objects.get(name_creator="Грюнмед")
    return render(request, 'grunmed.html', {'grun': grun})


def shitter(request):
    shtt = Creator.objects.get(name_creator="Шиттер")
    return render(request, 'shitter.html', {'shtt': shtt})


def glad(request):
    gl = Creator.objects.get(name_creator="Гладь")
    return render(request, 'glad.html', {'gl': gl})


@login_required(login_url='login')
def shipper(request):
    shipp = Shipper.objects.all()
    return render(request, 'shipper.html', {'shipp': shipp})


@login_required(login_url='login')
def supply(request):
    sup = Supply.objects.all()
    sup_comp = Supply_compos.objects.all()
    return render(request, 'supply.html', {'sup': sup, 'sup_comp': sup_comp})


@login_required(login_url='login')
def sale(request):
    sal = Sale.objects.all()
    sal_comp = Sale_compos.objects.all()
    sal_c = Sale_compos.objects.filter(sale_id__id=1)
    return render(request, 'sale.html', {'sal': sal, 'sal_comp': sal_comp, 'sal_c': sal_c})


def addsupply(request):
    if request.method == 'POST':
        form = AddSupply(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addsupplycomp')
    else:
        form = AddSupply()
    return render(request, 'addsupply.html', {'form': form})


def addsale(request):
    if request.method == 'POST':
        form = AddSale(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addsalecomp')
    else:
        form = AddSale()
    return render(request, 'addsale.html', {'form': form})


def addsalecomp(request):
    if request.method == 'POST':
        form = AddSaleComp(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sale')
    else:
        form = AddSaleComp()
    return render(request, 'addsalecomp.html', {'form': form})


def addadress(request):
    if request.method == 'POST':
        form = AddAdress(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AddAdress()
    return render(request, 'add_adress.html', {'form': form})


def addsupplycomp(request):
    if request.method == 'POST':
        form = AddSupplyComp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supply')
    else:
        form = AddSupplyComp()
    return render(request, 'addsupplycomp.html', {'form': form})


class EditAdress(ModelFormWidgetMixin, UpdateView):
    model = Adress
    template_name = 'editadress.html'
    success_url = reverse_lazy('profile')
    fields = {'country', 'city', 'street', 'num_house', 'num_apart'}
    widgets = {
        'country': forms.TextInput(attrs={'class': 'myfield'}),
        'city': forms.TextInput(attrs={'class': 'myfield'}),
        'street': forms.TextInput(attrs={'class': 'myfield'}),
        'num_house': forms.NumberInput(attrs={'class': 'myfield'}),
        'num_apart': forms.NumberInput(attrs={'class': 'myfield'}),
    }


class EditSale(ModelFormWidgetMixin, UpdateView):
    model = Sale
    template_name = 'editsale.html'
    success_url = reverse_lazy('sale')
    fields = ['user_id', 'datetime_sale']
    widgets = {'datetime_sale': forms.DateTimeInput(attrs={'class': 'myfield'})}


class EditSaleComp(ModelFormWidgetMixin, UpdateView):
    model = Sale_compos
    template_name = 'editsalecomp.html'
    success_url = reverse_lazy('sale')
    fields = ['sale_id', 'med_id', 'quantity_sale', 'recept_photo']
    widgets = {'quantity_sale': forms.NumberInput(attrs={'class': 'myfield'})}


class DeleteAdress(DeleteView):
    model = Adress
    template_name = 'deleteadress.html'
    success_url = reverse_lazy('profile')


class DeleteSale(DeleteView):
    model = Sale
    template_name = 'deletesale.html'
    success_url = reverse_lazy('sale')


class DeleteSaleComp(DeleteView):
    model = Sale_compos
    template_name = 'deletesalecomp.html'
    success_url = reverse_lazy('sale')


class EditSupply(ModelFormWidgetMixin, UpdateView):
    model = Supply
    template_name = 'editsupply.html'
    success_url = reverse_lazy('supply')
    fields = ['shipper_id', 'datetime_supply']
    widgets = {'datetime_supply': forms.DateTimeInput(attrs={'class': 'myfield'})}


class EditSupplyComp(ModelFormWidgetMixin, UpdateView):
    model = Supply_compos
    template_name = 'editsupplycomp.html'
    success_url = reverse_lazy('supply')
    fields = ['supply_id', 'med_id', 'quantity_supply']
    widgets = {'quantity_supply': forms.NumberInput(attrs={'class': 'myfield'})}


class DeleteSupply(DeleteView):
    model = Supply
    template_name = 'deletesupply.html'
    success_url = reverse_lazy('supply')


class DeleteSupplyComp(DeleteView):
    model = Supply_compos
    template_name = 'deletesupplycomp.html'
    success_url = reverse_lazy('supply')


class EditProf(ModelFormWidgetMixin, UpdateView):
    model = User
    template_name = 'editprof.html'
    success_url = reverse_lazy('profile')
    fields = ['user_photo', 'first_name', 'last_name', 't_name', 'username', 'email', 'adress_id',
              'name_company', 'INN', 'KPP', 'phone_number', 'date_birth']
    widgets = {
        'first_name': forms.TextInput(attrs={'class': 'myfield'}),
        'last_name': forms.TextInput(attrs={'class': 'myfield'}),
        't_name': forms.TextInput(attrs={'class': 'myfield'}),
        'username': forms.TextInput(attrs={'class': 'myfield'}),
        'email': forms.EmailInput(attrs={'class': 'myfield'}),
        'name_company': forms.TextInput(attrs={'class': 'myfield'}),
        'INN': forms.NumberInput(attrs={'class': 'myfield'}),
        'KPP': forms.NumberInput(attrs={'class': 'myfield'}),
        'phone_number': forms.NumberInput(attrs={'class': 'myfield'}),
        'date_birth': forms.DateInput(attrs={'class': 'myfield'}),
    }


def profile(request):
    prof = User.objects.all()
    return render(request, 'profile.html', {'prof': prof})


class Register(CreateView):
    model = User
    template_name = 'reg.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')
    success_msg = 'Регистрация прошла успешна'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid


class Login(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return self.success_url


class Logout(LogoutView):
    next_page = reverse_lazy('login')
