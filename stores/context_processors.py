from .models import Store
from django.shortcuts import get_object_or_404

def my_store(request):
    store=get_object_or_404(Store, owner_id=request.user.id)
    return {'my_store':store}