from django.urls import path
from . import views

urlpatterns=[
    path('users/', views.UserListView.as_view()),
    path('products/', views.ProductListView.as_view()),
    path('', views.ProductListView.as_view()),
    path('stores/', views.StoreListView.as_view()),
    path('products-categories/', views.CategoryListView.as_view()),
]
