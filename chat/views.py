from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json

@login_required
def chat_room(request):
    return render(request, 
                'chat/room.html', 
                {'username':mark_safe(json.dumps(request.user.username))})
