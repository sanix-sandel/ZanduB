from django.db import models
import uuid
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import (
    GenericForeignKey,
    GenericRelation
)
from taggit.managers import TaggableManager

class Category(models.Model):
    id=models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False
    )

    name=models.CharField(max_length=200,
                            db_index=True)
    logo=models.ImageField(upload_to='categories_pics/', blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='categorie'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name



class Product(models.Model):
    id=models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False
    )
    owner_ct=models.ForeignKey(ContentType, blank=False,
                                null=False,
                                related_name='products',
                                on_delete=models.CASCADE)

    owner_id=models.UUIDField(null=False, blank=False,
                                        db_index=True)

    owner=GenericForeignKey('owner_ct', 'owner_id')
    title=models.CharField(max_length=100)
    font_image=models.ImageField(upload_to='font_images/',
                                blank=False,
                                null=False)
    category=models.ForeignKey(Category, related_name='product',
                                on_delete=models.CASCADE)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    likes=models.ManyToManyField(settings.AUTH_USER_MODEL,
                                blank=True,
                                related_name='products_liked')
    tags = TaggableManager()                            
    views=models.PositiveIntegerField(default=0)
    available=models.BooleanField(default=True)
    date_posted=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    on_sale=models.BooleanField(default=False)

    class Meta:
        ordering=('-date_posted',)

    @property
    def onsale(self):
        return self.updated!=self.date_posted
        #self.on_sale

    @onsale.setter
    def get_onsale(self):
        if self.updated!=self.date_posted:
            self.on_sale=True




    def __str__(self):
        return f"{self.title} uploaded by {self.owner}"



class ProductImage(models.Model):
    id=models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    product=models.ForeignKey(Product, related_name='image',
                                on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products_pics/', blank=True)

    def __str__(self):
        return f"image belonging to {self.product}"



class ProductComment(models.Model):
    id=models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    content=models.CharField(max_length=300)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='comment', on_delete=models.CASCADE)
    date_posted=models.DateTimeField(auto_now_add=True)
