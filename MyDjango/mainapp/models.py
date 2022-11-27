from django.db import models
from django import forms
# Create your models here.
#  модель автомобиля
class Car(models.Model):
    """"Car models"""
    class Meta:
        verbose_name=u'Автомобиль'
        verbose_name_plural=u'Автомобили'


    car_name = models.ForeignKey('Manufacture',verbose_name=u'Марка автомобиля',blank=False,null=True,
                                          on_delete=models.PROTECT)
    last_name = models.CharField(max_length=100,blank=False,verbose_name=u"Модель автомобиля")
    vin = models.CharField(max_length=17,blank=True,null=False,verbose_name=u"Вин номер")
    car_class=models.CharField(max_length=2,blank=True,null=False,verbose_name=u"Класс автомобиля")
    year_of_release = models.IntegerField(blank=False,verbose_name=u"Год выпуска")
    type_body = models.CharField(max_length=50,blank=False,verbose_name=u"Тип кузова")
    drive = models.CharField(max_length=50,blank=False,verbose_name=u"Тип привода")
    fuel = models.CharField(max_length=50,blank=False,verbose_name=u"Вид топлива")
    volume_engine = models.FloatField(blank=False,verbose_name=u"Рабочий обьем,куб.см")
    color = models.CharField(max_length=50,blank=False,verbose_name=u"Цвет")
    number_of_seats = models.IntegerField(blank=False,verbose_name=u"Колличество мест")
    maximum_speed = models.IntegerField(blank=False,verbose_name=u"Максимальная скорость,км/ч")
    curb_weight = models.IntegerField(blank=False,verbose_name=u"Снаряженная масса,кг")
    euroncap =models.IntegerField(blank=False,verbose_name=u"рейтинг безопасности автомобилей euroncap (кол-во звезд)")
    price = models.IntegerField(blank=False,verbose_name=u"Цена(y.e.)")
    photo = models.ImageField(blank=True,null=True,verbose_name=u"Фото",upload_to='image_car')
    notes = models.TextField(blank=True,verbose_name=u"Доп. информация")
    create_at = models.DateTimeField(auto_created=True)
    avtosalon_group = models.ForeignKey('Stock',verbose_name=u'Автосалон',blank=False,null=True,
                                          on_delete=models.PROTECT)

    def __str__(self):
        return f'Автомобиль {self.car_name} {self.last_name}'










class Manufacture(models.Model):
    """"Manufacture model"""

    class Meta:
        verbose_name = u"Производитель"
        verbose_name_plural = u'Производители'

    manufacture_name = models.CharField(max_length=50,blank=False,verbose_name=u"Названия компании")
    country_of_manufacture= models.CharField(max_length=50,blank=False,verbose_name=u"Страна производства")
    date_of_foundation = models.CharField(max_length=50,blank=False,verbose_name=u"Дата основания компании")
    history = models.TextField(blank=True, null=True,verbose_name=u"История компании")
    logo_manuf = models.ImageField(blank=True, null=True, verbose_name=u"Логотип",upload_to='logo')

    def __repr__(self):
        return f'Производитель - {self.manufacture_name} - страна {self.country_of_manufacture}'





# Салоны

class Stock(models.Model):
    """"Stock model"""

    class Meta:
        verbose_name = u"Салон"
        verbose_name_plural = u'Салоны'

    name = models.CharField(max_length=50,blank=False,verbose_name=u"Название салона")
    sity = models.CharField(max_length=50,blank=False,verbose_name=u"Город")
    location = models.CharField(max_length=50,blank=False,verbose_name=u"Адрес")
    square = models.IntegerField(blank=True,null=True,verbose_name=u"Площадь склада,м.кв")
    number_of_seats = models.IntegerField(blank=True,null=True,verbose_name=u"Количество мест на складе")
    manager_shop = models.ForeignKey('Shop_manager',verbose_name=u'Менедер по продажам',blank=False,null=True,
                                           on_delete=models.PROTECT)
    top_manager = models.ForeignKey('Manager',verbose_name=u'Управляющий',blank=False,null=True,
                                           on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=50,blank=False,verbose_name=u"Номер телефона")
    foto = models.ImageField(blank=True, null=True, verbose_name=u"Фото шоурума", upload_to='foto_salon')


    def __repr__(self):
        return f'Cалон по продаже автомобилей {self.name} расположенный в городе {self.sity} по адресу {self.location}'






class Manager(models.Model):
    """"Manager model"""

    class Meta:
        verbose_name = u"Управляющий"
        verbose_name_plural = u'Управляющие'

    first_name = models.CharField(max_length=50,blank=False,verbose_name=u"Имя")
    last_name = models.CharField(max_length=50,blank=False,verbose_name=u"Фамилия")
    patronymic = models.CharField(max_length=50,blank=False,verbose_name=u"Отчество")
    phone_number = models.CharField(max_length=50, blank=False, verbose_name=u"Номер телефона")
    number_tm = models.IntegerField(blank=False, null=False, verbose_name=u"Табельный номер")
    create_at = models.DateTimeField(auto_created=True)
    avatar = models.ImageField(blank=True, null=True, verbose_name=u"Аватар", upload_to='ava')


    def __repr__(self):

            return f'Управляющий  {self.first_name} {self.last_name} {self.patronymic} '




class Shop_manager(models.Model):
    """"Manager shop"""

    class Meta:
        verbose_name = u"Менеджер по продажам"
        verbose_name_plural = u'Менеджеры по продажам'

    first_name = models.CharField(max_length=50, blank=False, verbose_name=u"Имя")
    last_name = models.CharField(max_length=50, blank=False, verbose_name=u"Фамилия")
    patronymic = models.CharField(max_length=50, blank=False, verbose_name=u"Отчество")
    phone_number = models.CharField(max_length=50, blank=False, verbose_name=u"Номер телефона")
    number_tm = models.IntegerField(blank=False, null=False, verbose_name=u"Табельный номер")
    # team = models.ForeignKey('Team',verbose_name=u'Подразделение',blank=False,null=True,
    #                                        on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_created=True)
    avatar = models.ImageField(blank=True, null=True, verbose_name=u"Аватар", upload_to='ava')

    def __repr__(self):
        return f'Менеджер  {self.first_name} {self.last_name} {self.patronymic} '




class Team(models.Model):
    """"Stock model"""

    class Meta:
        verbose_name = u"Отдел"
        verbose_name_plural = u'Отделы'

    name_team = models.CharField(max_length=50,blank=False,verbose_name=u"Название отдела")
    create_at = models.DateTimeField(auto_created=True, verbose_name=u"Дата основания отдела")
    top_employee = models.OneToOneField('Shop_manager', verbose_name=u"Сотрудник месяца", blank=True, null=True,
                                    on_delete=models.SET_NULL)




    def __repr__(self):
        if self.top_employee:
            return f'Лучший менеджер по продажам прошлого месяца {self.top_employee.first_name}' \
                   f' {self.top_employee.last_name}'

            return f"<Team {self.name_team}>"





class BaseContenerAuto(models.Model):


    class Meta:
        abstract = True

    title=models.CharField(max_length=100)

    create_ad = models.DateTimeField(
            auto_now_add=True,
            editable=False,
            blank=False,null=True,
        )

    update_at = models.DateTimeField(
            auto_now=True,
            editable=False,
            blank=False,null=True,
        )

    delete_at = models.CharField(default=False,max_length=10)



    def delete(self):
            self.delete_at = True
            self.save()




class Auto_service(BaseContenerAuto):

    car_brand = models.CharField(max_length=100)
    repair_plan = models.CharField(max_length=100)

    def __repr__(self):
         return f'Произвести  {self.title} на автомобиле {self.car_brand}.План работы: {self.repair_plan} '