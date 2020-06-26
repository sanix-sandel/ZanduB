from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)
from stores.models import Store
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserChangeForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

# Create your views here.# DEBUG:

class Update_Profile(LoginRequiredMixin, UpdateView):
    model=get_user_model()
    form_class=UserChangeForm
    success_url=reverse_lazy('products:home')
    template_name='account/profile.html'

