from django.urls import path, include
from . import views
from django.views.decorators.cache import cache_page


app_name='accounts'

urlpatterns = [
    path('profile/<uuid:pk>/', cache_page(60*15)(views.Update_Profile.as_view()), name='update_profile'),   
]
