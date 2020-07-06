from django.contrib.auth import get_user_model
from .serializers import *
from products.models import *
from stores.models import *


from rest_framework import generics



class UserListView(generics.ListAPIView):
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer


class ProductListView(generics.ListAPIView):
    queryset=Product.objects.all()    
    serializer_class=ProductSerilaizer


class StoreListView(generics.ListAPIView):
    queryset=Store.objects.all()
    serializer_class=StoreSerializer
