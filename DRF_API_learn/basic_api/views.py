from django.shortcuts import render
from basic_api.serializer import employee_serializer
from basic_api.models import employee_model
from rest_framework import viewsets
# Create your views here.


class UserViewset(viewsets.ModelViewSet):
    queryset=employee_model.objects.all()
    serializer_class=employee_serializer


