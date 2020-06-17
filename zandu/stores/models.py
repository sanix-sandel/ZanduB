from django.db import models
import uuid
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import (
    GenericForeignKey,
    GenericRelation
)


class Store(models.Model):
    id=models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    owner_ct=models.ForeignKey(ContentType, blank=False,
                                null=False,
                                related_name='own_store',
                                on_delete=models.CASCADE)
    owner_id=models.UUIDField(null=False, blank=False,
                                        db_index=True)

    owner=GenericForeignKey('owner_ct', 'owner_id')


    cover_image=models.ImageField(upload_to='store_pics/', blank=True)
    title=models.CharField(max_length=50)
    slogan=models.CharField(max_length=250)
    about=models.TextField()
    followers=models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name='stores_followed',
                                    blank=True)
    rate=models.PositiveIntegerField(default=0)
    products=GenericRelation("products.Product", content_type_field='owner_ct',
                            object_id_field='owner_id',
                            related_query_name='products')
    address=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)

#followers

    def __str__(self):
        return f"{self.title}-  belonging to {self.owner}"


class Post(models.Model):
    content=models.TextField()
    author=models.ForeignKey(Store, related_name='post', on_delete=models.CASCADE)
    date_uploaded=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"post belonging to {store}"
