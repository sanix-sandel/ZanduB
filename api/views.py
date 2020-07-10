from django.contrib.auth import get_user_model
from .serializers import *
from products.models import *
from stores.models import *


from rest_framework import generics, permissions



class UserListView(generics.ListAPIView):

    permissions_class=(permissions.IsAuthenticated,)
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer


class ProductListView(generics.ListAPIView):
    permissions_class=(permissions.IsAuthenticated,)
    queryset=Product.objects.all()    
    serializer_class=ProductSerializer


class StoreListView(generics.ListAPIView):
    permissions_class=(permissions.IsAuthenticated,)
    queryset=Store.objects.all()
    serializer_class=StoreSerializer


class CategoryListView(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer