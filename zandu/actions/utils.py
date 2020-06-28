from .models import Notification

def notify( verb, target, user=None):
    notification=Notification(user=user, verb=verb, target=target)
    notification.save()
    return True
