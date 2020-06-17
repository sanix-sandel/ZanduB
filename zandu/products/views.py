from django.shortcuts import render, get_object_or_404, redirect
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

#class Sell(CreateView):
#    model=Product
#    fields=['title', 'price', 'category', 'description']
#    success_url=reverse_lazy('home')
#    template_name='products/sell.html'

#    def form_valid(self, form):
#        form.instance.owner=self.request.user
#        return super().form_valid(form)


def Sell(request):
    if request.method=='POST':
        form=ProductForm(data=request.POST,
                        files=request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.owner=request.user
            product.save()
            return redirect('home')
        else:
            return redirect('stores')
    else:
        form=ProductForm()
    return render(request, 'products/sell.html', {'form':form})


def Home(request):
    products=Product.objects.all()

    context={
        'products':products,

    }
    return render(request, 'products/home.html', context)


def category(request, id):
    category=get_object_or_404(Category, id=id)
    categories=Category.objects.all()
    products=Product.objects.filter(category=category)
    context={
        'categories':categories,
        'category':category,
        'products':products
    }
    return render(request, 'products/bycategories.html', context)

def ProductView(request, id):
    product=get_object_or_404(Product, id=id)


    context={

        'product':product
    }
    return render(request, 'products/product.html', context)
