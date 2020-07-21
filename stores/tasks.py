from celery import task
from django.core.mail import send_mail
from django.contrib import messages
from actions.utils import notify

@task
def send():
   
    send_mail('Django mail', 
                'This e-mail was sent with Django.', 
                'your_account@gmail.com', 
                ['your_account@gmail.com'], 
                fail_silently=False
            )
   

@task
def notify_followers(followers=[]):
    if len(followers)==True:
        for follower in followers:
            notify(user=request.user, verb='a fait une annonce', target=follower)
        