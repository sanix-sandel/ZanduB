from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import*
from accounts.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
   
    product=serializers.ReadOnlyField(source='product.title')
    class Meta:
        model=Category
        fields='__all__'    

class ProductSerializer(serializers.ModelSerializer):
   # category=CategorySerializer()
    category=serializers.ReadOnlyField(source='category.name')#get the name
    likes=UserSerializer(many=True)#nested
    class Meta:
        model=Product
        fields='__all__'

class ProductActionSerializer(serializers.Serializer):
    id=serializers.UUIDField()        

    """# product=serializers.HyperlinkedModelSerializer(
    #    many=True,
    #    read_only=True,
    #    view_name='product_detail'
    #)"""