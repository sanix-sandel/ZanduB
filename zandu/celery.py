import os 
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zandu.settings')

app=Celery('zandu')

app.config_from_object('django.conf:settings', namespace='CELERY')
#by setting he CELERY namespace, all Celery settings need to include the
#CELERY_ prefix in their name (for example, CELERY_BROKER_URL ).
app.autodiscover_tasks()#celery to autodiscover asynchronous tasks

#In the __init__.py file celery module must be imported