from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.StoresList, name='stores'),
    path('<uuid:id>/', views.StoreView, name='view_store'),
]
