from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import*

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields='__all__'    

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Product
        fields='__all__'

class ProductActionSerializer(serializers.Serializer):
    id=serializers.UUIDField()        