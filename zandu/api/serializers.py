from django.contrib.auth import get_user_model
from rest_framework import serializers
from stores.models import *
from products.models import *
from actions.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields='__all__'


class ProductSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class StoreSerializer(serializers.ModelSerializer):
    model=Store
    fields='__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'    