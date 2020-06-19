from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm


def cart_add(request, product_id):
    cart=Cart(request)
    product=get_object_or_404(Product, id=product_id)
    form=CartAddProductForm(require.POST)
    if form.is_valid():
        cd=form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                override_quantity=cd['override'])
    return redirect('cart:detail')            
