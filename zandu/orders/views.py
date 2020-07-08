from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
#from .tasks import order_created
from django.urls import reverse
from django.shortcuts import render, redirect


def order_create(request, cart_id):
    cart=Cart(request, cart_id)#we'll obtain the current cart from session
    if request.method=='POST':
        form=OrderCreateForm(request.POST)
        if form.is_valid():
            order=form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            #Clear the cart
            cart.clear()
        #    order_created.delay(order.id)
            request.session['order_id']=order.id#set the order in the session
            return redirect('products:home')#redirect(reverse('payment:process'))#for payment
    else:#Get request instanciates the OrderCreateForm form and renders the
        #orders/order/create.html
        form=OrderCreateForm()
    return render(request,
                 'orders/create.html',
                 {'cart':cart, 'form':form})

