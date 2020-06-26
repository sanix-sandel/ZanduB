from celery import task
from django.core.mail import send_mail
from django.contrib import messages

@task
def send():
   
    send_mail('Django mail', 
                'This e-mail was sent with Django.', 
                'your_account@gmail.com', 
                ['your_account@gmail.com'], 
                fail_silently=False
            )
   

