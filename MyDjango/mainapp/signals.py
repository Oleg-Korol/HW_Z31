from uuid import uuid4
from datetime import datetime
from .models import Car
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save,sender=Car,dispatch_uid = uuid4())
def create_custom(sender,**kwargs):

    with open("static/txt/Postavki.txt",  'a',encoding='utf-8') as file:
        file.write(f"{datetime.now()}   Добавился новый авто на склад!Подробная информация у менеджера по продажам"+ '\n')
