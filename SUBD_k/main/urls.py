from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.admin, name='admin/'),
    path('catalog1', views.catalog1, name='catalog1'),
    path('grunmed', views.grunmed, name='grunmed'),
    path('shitter', views.shitter, name='shitter'),
    path('glad', views.glad, name='glad'),
    path('addsupply/', views.addsupply, name='addsupply'),
    path('addsale/', views.addsale, name='addsale'),
    path('addsupplycomp/', views.addsupplycomp, name='addsupplycomp'),
    path('addsalecomp/', views.addsalecomp, name='addsalecomp'),
    path('add_adress/', views.addadress, name='add_adress'),
    path('shipper', views.shipper, name='shipper'),
    path('supply', views.supply, name='supply'),
    path('sale', views.sale, name='sale'),
    path('profile', views.profile, name='profile'),
    path('/<int:pk>/editadress', EditAdress.as_view(), name='editadress'),
    path('/<int:pk>/editprof', EditProf.as_view(), name='editprof'),
    path('/<int:pk>/editsale', EditSale.as_view(), name='editsale'),
    path('/<int:pk>/editsalecomp', EditSaleComp.as_view(), name='editsalecomp'),
    path('/<int:pk>/deleteadress', DeleteAdress.as_view(), name='deleteadress'),
    path('/<int:pk>/deletesale', DeleteSale.as_view(), name='deletesale'),
    path('/<int:pk>/deletesalecomp', DeleteSaleComp.as_view(), name='deletesalecomp'),
    path('/<int:pk>/editsupply', EditSupply.as_view(), name='editsupply'),
    path('/<int:pk>/editsupplycomp', EditSupplyComp.as_view(), name='editsupplycomp'),
    path('/<int:pk>/deletesupply', DeleteSupply.as_view(), name='deletesupply'),
    path('/<int:pk>/deletesupplycomp', DeleteSupplyComp.as_view(), name='deletesupplycomp'),
    path('login', views.Login.as_view(), name='login'),
    path('reg', views.Register.as_view(), name='reg'),
    path('logout', views.Logout.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)