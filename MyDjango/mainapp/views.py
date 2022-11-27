from . models import*
from django.shortcuts import render


def index(request):

      return render(request,'mainapp/index.html',{'title':'Главная страница'} )

def manufacture(request):
      man = Manufacture.objects.all()
      return render(request,'mainapp/man_list.html',{'title':'Производители','man':man} )




def cars(request):
      auto = Car.objects.all()
      return render(request,'mainapp/car_list.html',{'title':'Автомобили в наличии','auto':auto} )


def salon(request):
      salon = Stock.objects.all()
      return render(request,'mainapp/salon.html',{'title':'Наши салоны','salon':salon} )



def manager(request):
      manager = Manager.objects.all()
      return render(request,'mainapp/manager.html',{'title':'Руководство компании','manager':manager} )


def manager_shop(request):
      manshop =Shop_manager.objects.all()
      return render(request,'mainapp/manager_shop.html',{'title':'Менеджеры продаж','manshop':manshop} )


def otdel(request):
      otdel =Team.objects.all()
      return render(request,'mainapp/team.html',{'title':'Отделы','otdel':otdel} )


def about(request):
       return render(request, 'mainapp/about.html')


def contact(request):
      return render(request, 'mainapp/contact.html')

