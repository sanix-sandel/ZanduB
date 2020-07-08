from django.shortcuts import render
from taggit.models import Tag

def products_by_tag(request, tag_slug=None):
    if tag_slug==None:
        return redirect('products:home')
    else:    
        tag = get_object_or_404(Tag, slug=tag_slug)
        products = Product.objects.filter(tags__in=[tag])
        context={
            'products':products,
            'tag':tag
        }
        return render(request, 'tags/products.html', context)