from django.db.models import Q
from products.models import Product
from django.views.generic import ListView

class Search(ListView):
    model=Product
    template_name='search/results.html'
    context_object_name='products'

    def get_queryset(self):
        query=self.request.GET.get('q')
        return Product.objects.filter(
            Q(title__icontains=query)|Q(description__icontains=query)
        )