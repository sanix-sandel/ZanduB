from django.contrib.auth import get_user_model
from rest_framework import serializers
from stores.models import *
from products.models import *
from actions.models import *

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=get_user_model()
        fields=('id', 'username', 'email', 'profile_image', 'is_active', 'reports')

class StoreSerializer(serializers.ModelSerializer):
    #followers=UserSerializer(read_only=True)
    class Meta:
        model=Store
        fields='__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'       


class ProductSerializer(serializers.ModelSerializer):
  #  category=CategorySerializer()
  #  likes=UserSerializer()
    class Meta:
        model=Product
        fields=('id',)#'__all__'



 