from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Store, Post
from products.models import Category, Product
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)
from .forms import StoreForm, PostForm
from products.forms import ProductForm
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from actions.utils import notify

class StoresList(ListView):
    model=Store
    context_object_name='stores'
    template_name='stores/stores.html'

@login_required
def CreateStore(request):
    if request.method=='POST':
        form=StoreForm(request.POST, request.FILES)
        if form.is_valid():
            store=form.save(commit=False)
            store.owner=request.user
            store.save()
            request.session['store_id']=store.id#store middleware
            return redirect('stores:view_store', id=store.id)
    else:
        form=StoreForm()
    return render(request, 'stores/create_store.html',
                            {'form':form})



def StoreView(request, id):
    store=get_object_or_404(Store, id=id)
   # request.session['store_id']=store.id
    products=store.products.all()#Product.objects.filter(owner_id=store.id).all()
    context={
        'products':products,
        'store':store,

    }
    return render(request, 'stores/store.html', context)



@login_required
def AddProduct(request, store_id):
    store=get_object_or_404(Store, id=store_id)
    if request.method=='POST':
        form=ProductForm(data=request.POST,
                        files=request.FILES)
        if form.is_valid():
            product=form.save(commit=False)
            product.owner=store
            product.save()
            return redirect('stores:view_store', id=store.id)
    else:
        form=ProductForm()
    return render(request, 'stores/add_product.html',
                    {'form':form, 'store':store})

#class MakePost(CreateView):
#    model=Post
#    fields=('content',)
#    template_name='stores/make_post.html'
#    self.get_store()
#    store=None
#    def success_url(self):
#        return reverse_lazy('home')
#    def get_store(self, store_id):
#        print('Life is what')
#        self.store=get_object_or_404(Store, id=store_id)
#        return self.store
#    def form_valid(self, form):
#        print('you make it')
#        form.instance.author=self.get_store()
#        return super().form_valid(form)
@login_required
def MakePost(request, store_id):
    store=get_object_or_404(Store, id=store_id)
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=store
            post.save()
            return redirect('products:home')
    else:
        form=PostForm()
    return render(request, 'stores/make_post.html',
                {'form':form})



def PostList(request):
    stores_ids=Store.objects.filter(followers__in=request.user).values_list('id', flat=True)
    print (stores)
    posts=Post.objects.filter(author__id__in=stores_ids)
    context={
        'posts':posts
    }
    return render(request, 'stores/posts.html', context)


#follow a store
@login_required
def follow_store(request, store_id):
    store=get_object_or_404(Store, id=store_id)
    if not request.user in store.followers.all():
        store.followers.add(request.user)
        notify(user=request.user, verb='is following your store', target=store.owner)
       
    else:
        store.followers.remove(request.user)
    return redirect('stores:stores')


class UserMixin:
    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(followers__in=[self.request.user])


class FavouriteStores(UserMixin, ListView):
    model=Store
    context_object_name='stores'
    template_name='stores/favourite_stores.html'
