from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import*
from accounts.serializers import UserSerializer


class StoreSerializer(serializers.ModelSerializer):

    owner=UserSerializer()
    followers=UserSerializer(many=True, read_only=True)#nested
   # followers=serializers.StringRelatedField(many=True)
    #instead of StringRelatedField, PrimaryKeyrelatedField can be used
    #so id will be displayed
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


#SlugRelatedField may be used to represent the target of the relationship 
# using a field on the target(id, title, name,....).