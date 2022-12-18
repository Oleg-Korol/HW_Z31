from rest_framework.serializers import ModelSerializer

from mainapp.models import Car


class CarsSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ('last_name','year_of_release','price')