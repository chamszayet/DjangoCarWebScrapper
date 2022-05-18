from rest_framework import serializers
from .models import Car
from dataclasses import fields





class CarSerializer(serializers.ModelSerializer):
    class Meta:
       model = Car
       fields = '__all__'
