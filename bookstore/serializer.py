from rest_framework import serializers
from . import models

class bookserializer(serializers.Serializer):
    id=serializers.IntegerField()
    title=serializers.CharField(max_length=255)
    author=serializers.CharField(max_length=255)
    inventory=serializers.IntegerField()
    
    def create(self,validated_data):
        models.book.objects.create(**validated_data)
    def update(self,validated_data):
        models.book.objects.filter(id=validated_data.id).update(**validated_data)