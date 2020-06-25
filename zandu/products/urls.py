from django.urls import path, include
from . import views

app_name='products'

urlpatterns = [
    path('', views.Home, name='home'),
    path('category/<uuid:id>', views.category, name='bycategory'),
    path('product/<uuid:id>', views.ProductView, name='view_product'),
    path('product/sell', views.Sell.as_view(), name='sell'),
    path('product/like/<uuid:product_id>', views.like_product,
        name='like_product'),

    path('product/update/<uuid:pk>/', views.UpdateProduct.as_view(),
        name='update_product'),
    path('products_liked/', views.products_liked,
        name='products_liked'),    
]
