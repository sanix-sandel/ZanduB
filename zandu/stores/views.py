from django.shortcuts import render, get_object_or_404, redirect
from .models import Store
from products.models import Category, Product
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from .forms import StoreForm
from products.forms import ProductForm


class StoresList(ListView):
    model=Store
    context_object_name='stores'
    template_name='stores/stores.html'


def CreateStore(request):
    if request.method=='POST':
        form=StoreForm(request.POST, request.FILES)
        if form.is_valid():
            store=form.save(commit=False)
            store.owner=request.user
            store.save()
            return redirect('view_store', id=store.id)
    else:
        form=StoreForm()
    return render(request, 'stores/create_store.html',
                            {'form':form})



def StoreView(request, id):
    store=get_object_or_404(Store, id=id)

    products=store.products.all()#Product.objects.filter(owner_id=store.id).all()
    context={
        'products':products,
        'store':store,

    }
    return render(request, 'stores/store.html', context)


def AddProduct(request, store_id):
    store=get_object_or_404(Store, id=store_id)
    if request.method=='POST':
        form=ProductForm(data=request.POST,
                        files=request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.owner=store
            product.save()
            return redirect('view_store', id=store.id)
    else:
        form=ProductForm()
    return render(request, 'stores/add_product.html',
                    {'form':form, 'store':store})


#follow a store
def follow_store(request, store_id):
    store=get_object_or_404(Store, id=store_id)
    if not request.user in store.followers.all():
        store.followers.add(request.user)
    else:
        store.followers.remove(request.user)
    return redirect('stores')


class UserMixin:
    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(followers__in=[self.request.user])

class FavouriteStores(UserMixin, ListView):
    model=Store
    context_object_name='stores'
    template_name='stores/favourite_stores.html'
