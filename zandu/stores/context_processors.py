from .models import Store
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models.AnonymousUser
from django.contrib.auth.models import AnonymousUser



def mystore(request):
    if request.user!=AnonymousUser():
        mystore=get_object_or_404(Store, owner_id=request.user.id)
        return {'mystore':mystore}
