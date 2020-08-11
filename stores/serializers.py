from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import*
from accounts.serializers import UserSerializer

class StoreSerializer(serializers.ModelSerializer):

    owner=UserSerializer()
    class Meta:
        model=Store
        fields=('id',
            'title', 
            'cover_image', 
            'owner', 
            'slogan', 
            'about',
            'rate',
            'address',
            'date_created',
            'followers')

class StoreActionSerializer(serializers.Serializer):
    id=serializers.UUIDField()        