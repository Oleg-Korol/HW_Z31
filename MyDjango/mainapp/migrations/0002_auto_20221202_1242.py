# Generated by Django 3.2.15 on 2022-12-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='sale_price',
            field=models.IntegerField(null=True, verbose_name='Цена c учетом скидки(y.e.)'),
        ),
        migrations.AddField(
            model_name='sale',
            name='sale_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Название акции'),
        ),
    ]
