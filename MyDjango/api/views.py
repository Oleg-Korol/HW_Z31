from django.shortcuts import render
from rest_framework import filters

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView,GenericAPIView
from .serializers import CarsSerializer
from mainapp.models import Car
from .paginations  import StandartPagination


class CarList(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarsSerializer
    filter_backends = [filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['last_name','price']
    search_fields = ['price']
    ordering = ['car_name']
    pagination_class = StandartPagination


class CarDetail(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarsSerializer