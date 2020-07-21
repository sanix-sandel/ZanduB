from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import*


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

class OrderActionSerializer(serializers.Serializer):        
    id=serializers.UUIDField()