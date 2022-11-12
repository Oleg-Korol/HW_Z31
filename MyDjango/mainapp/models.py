from django.db import models

# Create your models here.

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    car_name = models.CharField(max_length=100,blank=True,null=False)
    last_name = models.CharField(max_length=100,blank=True,null=False)
    year_of_release = models.IntegerField(max_length=4,blank=True,null=False)
    type_body = models.CharField(max_length=50,blank=True,null=False)
    drive = models.CharField(max_length=50,blank=True,null=False)
    engine = models.CharField(max_length=50,blank=True,null=False)
    volume_engine = models.FloatField(max_length=3,blank=True,null=False)
    color = models.CharField(max_length=50,blank=True,null=False)
    number_of_seats = models.IntegerField(max_length=2,blank=True,null=False)
    price = models.IntegerField(max_length=6,blank=True,null=False)

    create_at = models.DateTimeField(auto_created=True)

    def __repr__(self):
        return f'Student {self.first_name} {self.last_name}'
