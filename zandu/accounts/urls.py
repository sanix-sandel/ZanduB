from django.urls import path, include
from . import views

app_name='accounts'

urlpatterns = [
    path('profile/<uuid:pk>/', views.Update_Profile.as_view(), name='update_profile'),
       
]
