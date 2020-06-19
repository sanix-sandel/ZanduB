from django.urls import path, include

from . import views

app_name='stores'

urlpatterns = [
    path('', views.StoresList.as_view(), name='stores'),
    path('create_store/', views.CreateStore, name='create_store'),
    path('<uuid:id>/', views.StoreView, name='view_store'),
    path('<uuid:store_id>/follow', views.follow_store, name='follow_store'),
    path('<uuid:store_id>/addproduct/', views.AddProduct, name='add_product'),
    path('<uuid:store_id>/make_post/', views.MakePost, name='make_post'),
    path('favourite_stores/', views.FavouriteStores.as_view(),
        name='favourite_stores'),
]
