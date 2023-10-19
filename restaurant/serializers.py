from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name','temp']

class MenuItemSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model=MenuItem
        fields=['id','item','price','inventory','category']
