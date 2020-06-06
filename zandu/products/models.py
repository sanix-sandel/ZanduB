from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import (
    GenericForeignKey,
    GenericRelation
)


class Category(models.Model):
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
    owner_ct=models.ForeignKey(ContentType, blank=False,
                                null=False,
                                related_name='products',
                                on_delete=models.CASCADE)
                                
    owner_id=models.PositiveIntegerField(null=False, blank=False,
                                        db_index=True)

    title=models.CharField(max_length=100)

    category=models.ForeignKey(Category, related_name='product',
                                on_delete=models.CASACDE)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    likes=models.ManyToManyField(settings.AUTH_USER_MODEL,
                                related_name='products_liked')
    views=models.PositiveIntegerField(default=0)
    available=models.BooleanField(default=True)
    date_posted=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    on_sale=models.BooleanField(default=False)


    def __str__(self):
        return f"{self.title} uploaded by {self.uploader}"



class ProductImage(models.Model):
    product=models.ForeignKey(Product, related_name='image',
                                on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products_pics/', blank=True)

    def __str__(self):
        return f"image beloging of{self.product}"



class ProductComment(models.Model):
    content=CharField(max_length=300)
    author=models.ForeignKey(setiings.AUTH_USER_MODEL,
                            related_name='comment', on_delete=models.CASCADE)
    date_posted=models.DateTimeField(auto_add_now=True)
