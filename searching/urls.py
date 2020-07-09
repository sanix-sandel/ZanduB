from django.urls import path, include
from . import views

app_name='searching'

urlpatterns = [
    path('', views.Search.as_view(), name='search'),
       
]
