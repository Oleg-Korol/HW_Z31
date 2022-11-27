from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name = "home"),
    path('cars',views.cars,name =  'avto'),
    path('manufacture',views.manufacture,name =  'manufacture'),
    path('salon',views.salon,name =  'salon'),
    path('manager',views.manager,name =  'manager'),
    path('manshop',views.manager_shop,name =  'manager_shop'),
    path('team',views.otdel,name =  'team'),
    path('about',views.about,name =  'about'),
    path('contact',views.contact,name =  'contact'),
    ]