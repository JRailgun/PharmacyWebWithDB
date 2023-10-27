from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Med_group, Adress, Shipper, Creator, Med, Sale, User, Sale_compos, Supply, Supply_compos

admin.site.register(Med_group)
admin.site.register(Adress)
admin.site.register(Shipper)
admin.site.register(Creator)
admin.site.register(Med)
admin.site.register(Sale)
admin.site.register(Sale_compos)
admin.site.register(Supply)
admin.site.register(Supply_compos)

fields = list(UserAdmin.fieldsets)
fields[0] = (None, {'fields': ('username', 'password', 't_name', 'name_company', 'INN', 'KPP', 'date_birth', 'phone_number', 'user_photo')})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(User, UserAdmin)