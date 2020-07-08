from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@require_POST #only post request
def cart_add(request, product_id, cart_id, store_id):
    cart=Cart(request, cart_id)
    product=get_object_or_404(Product, id=product_id)
    form=CartAddProductForm(request.POST)
    if form.is_valid():
        cd=form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                override_quantity=cd['override'])
    return redirect('cart:cart_detail', 
                    cart_id=cart_id, 
                    store_id=store_id)

#The require_POST decorator
#returns an HttpResponseNotAllowed object (status code 405 )
#if the HTTP request
#is not done via POST . This way,
#you only allow POST requests for this view.

@require_POST
def cart_remove(request, product_id, cart_id):
    cart=Cart(request, cart_id)
    product=get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail', cart_id=cart_id)


def cart_detail(request, cart_id, store_id):
    from stores.models import Store
    store=get_object_or_404(Store, id=store_id)
    cart=Cart(request, cart_id)
    context={
        'cart':cart,
        'store':store
    }
    return render(request, 'stores/store_cart.html', context)
