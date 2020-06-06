from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import (
    GenericForeignKey,
    GenericRelation
)

class Store(models.Model):
    owner_ct=models.ForeignKey(ContentType, blank=False,
                                null=False,
                                related_name='own_store',
                                on_delete=models.CASCADE)
    owner_id=models.PositiveIntgerField(null=False, blank=False,
                                        db_index=True)

    owner=GenericForeignKey('owner_ct', 'owner_id')                                                                


    image=models.ImageField(upload_to='store_pics/', blank=True)
    title=models.CharField(max_length=50)
    slogan=models.CharField(max_length=250)
    about=models.TextField()
    followers=models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name='stores_followed',
                                    blank=True)
    rate=models.PositiveIntegerField()
    address=models.TextField()
    date_created=models.DateTimeField(auto_add_now=True)

#followers

    def __str__(self):
        return f"store belonging to {store.onwer}"


class Post(models.Model):
    content=models.TextField()
    author=models.ForeignKey(Store, related_name='post', on_delete=models.CASCADE)
    date_uploaded=models.DateTimeField(auto_add_now=True)

    def __str__(self):
        return f"post belonging to {store}"
