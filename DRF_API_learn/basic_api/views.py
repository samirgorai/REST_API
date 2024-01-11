from django.shortcuts import render
from basic_api.serializer import employee_serializer
from basic_api.models import employee_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class UserViewset(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset=employee_model.objects.all()
    serializer_class=employee_serializer



