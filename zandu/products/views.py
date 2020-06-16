from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from .models import Product, Category


def Home(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    context={
        'products':products,
        'categories':categories
    }
    return render(request, 'products/home.html', context)


def category(request, id):
    category=get_object_or_404(Category, id=id)
    products=Product.objects.filter(category=category)
    context={
        'category':category,
        'products':products
    }
    return render(request, 'products/bycategories.html', context)
