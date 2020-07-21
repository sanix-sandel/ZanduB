from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import*

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=('id', 'username', 'email', 'profile_image', 'is_active', 'reports')


class UserActionSerializer(serializers.Serializer):
    id=serializers.UUIDField()
    action=serilaizers.CharField()
    