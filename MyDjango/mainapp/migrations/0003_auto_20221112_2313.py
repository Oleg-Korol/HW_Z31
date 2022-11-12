# Generated by Django 3.2.15 on 2022-11-12 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20221112_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('create_at', models.DateTimeField(auto_created=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('car_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('year_of_release', models.IntegerField(blank=True, max_length=4)),
                ('type_body', models.CharField(blank=True, max_length=50)),
                ('drive', models.CharField(blank=True, max_length=50)),
                ('engine', models.CharField(blank=True, max_length=50)),
                ('volume_engine', models.FloatField(blank=True, max_length=3)),
                ('color', models.CharField(blank=True, max_length=50)),
                ('number_of_seats', models.IntegerField(blank=True, max_length=2)),
                ('price', models.IntegerField(blank=True, max_length=6)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]