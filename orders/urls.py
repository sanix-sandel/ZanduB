from django.urls import path
from . import views

app_name='orders'

urlpatterns=[
    path('create/<str:cart_id>/', views.order_create, name='order_create'),
]