from rest_framework import serializers
from basic_api.models import employee_model

class employee_serializer(serializers.ModelSerializer):
    class Meta:
        model=employee_model
        fields="__all__"