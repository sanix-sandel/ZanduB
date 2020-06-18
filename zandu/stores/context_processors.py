from .models import Store
from django.shortcuts import get_object_or_404

def mystore(request):
    mystore=get_object_or_404(Store, owner_id=request.user.id)
    return {'mystore':mystore}
