from django.urls import path, include

from . import views

app_name='cart'

urlpatterns = [
    path('cart/<str:cart_id>/<uuid:store_id>/', views.cart_detail,  name='cart_detail'),
    path('add/<uuid:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<uuid:product_id>/', views.cart_remove,
        name='cart_remove'),
]
