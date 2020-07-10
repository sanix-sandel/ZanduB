from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from .models import Product, Category
from .forms import ProductForm
from django.urls import reverse_lazy
from cart.forms import CartAddProductForm
from actions.utils import notify
from django.core.cache import cache
from django.contrib import messages

from api.serializers import ProductSerializer




class OwnerMixin(object):
    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(owner=self.request.user)


class Sell(LoginRequiredMixin, CreateView):
    model=Product
    fields=['title', 'font_image', 'category', 'price', 'description']
    success_url=reverse_lazy('products:home')
    template_name='products/sell.html'

    def form_valid(self, form):
        form.instance.owner=self.request.user
        return super().form_valid(form)


class UpdateProduct(LoginRequiredMixin, OwnerMixin, UpdateView):
    model=Product
    fields=['title', 'font_image', 'category', 'price', 'description']
    success_url=reverse_lazy('products:home')
    template_name='products/sell.html'
#def Sell(request):
#    if request.method=='POST':
#        form=ProductForm(data=request.POST,
#                        files=request.FILES)
#        if form.is_valid():
#            product=form.save(commit=False)
#            product.owner=request.user
#            product.save()
#            return redirect('home')
#        else:
#            return redirect('stores')
#    else:
#        form=ProductForm()
#    return render(request, 'products/sell.html', {'form':form})


def Home(request):
    products=cache.get('all_products')
    if not products:
        products=Product.objects.all()
        cache.set('all_products', products)
    context={
        'products':products,
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


def ProductView(request, id):
    from stores.models import Store
    from cart.cart import Cart

    product=get_object_or_404(Product, id=id)
    if type(product.owner)==Store:
        cart_product_form=CartAddProductForm(request.POST)
        store=get_object_or_404(Store, id=product.owner.id)
        cart_id=str(request.user)+str(product.owner.id)
        context={
            'cart_product_form':cart_product_form,
            'product':product,
            'store_id':product.owner.id,
            'store':store,
            'cart_id':cart_id
        }
        
        if cart_product_form.is_valid():
            
            cd=cart_product_form.cleaned_data
            cart=Cart(request, cart_id)

            cart.add(product=product, 
                    quantity=cd['quantity'], 
                    override_quantity=cd['override'])
            

            return redirect('cart:cart_detail', 
                    cart_id=cart_id, 
                    store_id=product.owner.id)
        print('an error')
        return render(request, 'stores/product_detail.html', context)
    else:
        context={

            'product':product
        }
        return render(request, 'products/product.html', context)


#comment about the product
@login_required
def like_product(request, product_id):
    product=get_object_or_404(Product, id=product_id)
    if request.user in product.likes.all():
        product.likes.remove(request.user)
    else:
        product.likes.add(request.user)
        print('article liked')
        notify(user=request.user, verb='a aime votre article', target=product.owner)
        print('notification sent')
    return redirect('products:view_product', id=product_id)


@login_required
def like_product_by_api(request, *args, **kwargs):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        
        product_id=data.get("id")
        product=get_object_or_404(Product, id=product_id)
        if request.user in product.likes.all():
            product.likes.remove(request.user)
            serializer=ProductSerializer(product)
            print('arcticle disliked')
            return Response({serializer.data}, status=200)
            
        else:
            product.likes.add(request.user)
            print('article liked')
            serializer=ProductSerializer(product)
            notify(user=request.user, verb='a aime votre article', target=product.owner)
            
            return Response({serializer.data}, status=200)
    return Response({}, status=200)



@login_required
def products_liked(request):
    user=request.user
    products=user.products_liked.all()
    context={
        'products':products
    }
    return render(request, 'products/products_liked.html', context)