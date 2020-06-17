from django.shortcuts import render, get_object_or_404
from .models import Store
from products.models import Category, Product

def StoresList(request):
    stores=Store.objects.all()

    context={
        'stores':stores,

    }
    return render(request, 'stores/stores.html', context)


def StoreView(request, id):
    store=get_object_or_404(Store, id=id)

    products=store.products.all()#Product.objects.filter(owner_id=store.id).all()
    context={
        'products':products,
        'store':store,
    
    }
    return render(request, 'stores/store.html', context)
