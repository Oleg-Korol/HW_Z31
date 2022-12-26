from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .forms import ManagerFormAdmin
from .models import *


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name_team', 'top_employee']
    list_display_links = ['name_team', 'top_employee']
    ordering = ['name_team']
    list_filter = ['name_team']
    list_per_page = 5
    search_fields = ['name_team', 'top_employee']

class Shop_manager_Admin(admin.ModelAdmin):
     list_display = ['last_name','first_name','patronymic','manager_team',
                     'custom_field','ava' ]
     list_display_links = ['last_name','first_name']
     list_editable = ['manager_team']
     list_filter = ['last_name',
                    'first_name',
                    'patronymic',
                    'manager_team',
                    'phone_number',
                    ]
     search_fields = ['last_name']
     list_per_page = 5
     ordering = ['last_name']
     form = ManagerFormAdmin

     @staticmethod
     def ava(obj):
         return mark_safe(f'<img src="{obj.avatar.url}"width="100">')

     @staticmethod
     def custom_field(obj):
         return mark_safe('<a href ="https://www.google.ru">Google</a>')

     # @staticmethod
     # def view_on_site(obj):
     #     return reverse('shop_manager-edit',kwargs = {'pk':obj.id})

# Register your models here.
admin.site.register(Car)
admin.site.register(Stock)
admin.site.register(Manufacture)
admin.site.register(Manager)
admin.site.register(Shop_manager,Shop_manager_Admin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Auto_service)
admin.site.register(Sale)
admin.site.register(MothJournal)
admin.site.register(Topic)
admin.site.register(Record)

