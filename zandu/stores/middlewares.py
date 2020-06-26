from . import models

def store_middleware(get_response):
    def middleware(request):
        if 'store_id' in request.session:
            store_id=request.session['store_id']
            store=models.Store.objects.get(id=store_id)
            request.store=store
        else:
            request.store=None
        
        response=get_response(request)
        return response
    return middleware            