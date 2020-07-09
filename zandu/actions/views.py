from django.shortcuts import render
from .models import Notification
from django.contrib.auth.decorators import login_required

@login_required
def notifications(request):
    user=request.user
    #notifs=Notification.objects.filter(target_id=user.id)
    notifs=user.notif.all()
    context={
        'notifs':notifs
    }
    return render(request, 'actions/notifs.html', context)
