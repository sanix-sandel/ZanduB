from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('category/<uuid:id>', views.category, name='bycategory'),
    path('product/<uuid:id>', views.ProductView, name='view_product'),
    path('product/sell', views.Sell.as_view(), name='sell'),
]
