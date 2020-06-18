from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.StoresList.as_view(), name='stores'),
    path('create_store/', views.CreateStore, name='create_store'),
    path('<uuid:id>/', views.StoreView, name='view_store'),
    path('<uuid:store_id>/follow', views.follow_store, name='follow_store'),
    path('<uuid:store_id>/addproduct/', views.AddProduct, name='add_product'),
    path('favourite_stores/', views.FavouriteStores.as_view(),
        name='favourite_stores'),
]
