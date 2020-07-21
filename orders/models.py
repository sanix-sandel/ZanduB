from django.db import models
import uuid
from products.models import Product
from django.conf import settings

class Order(models.Model):

    id=models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False
    )

    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.CharField(max_length=250)
    postal_code=models.CharField(max_length=20)
    city=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    paid=models.BooleanField(default=False)

    customer=models.ForeignKey(settings.AUTH_USER_MODEL,
                                related_name='orders',
                                on_delete=models.CASCADE)
    store=models.ForeignKey("stores.Store", related_name='orders', on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.BooleanField(default=False)
    paid=models.BooleanField(default=False)

    class Meta:
        ordering=('-created',)

    def __str__(self):
        return f"order by {self.customer.username}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())



class OrderItem(models.Model):
    order=models.ForeignKey(Order, related_name='items',
                            on_delete=models.CASCADE)
    product=models.ForeignKey(Product, related_name='order_items',
                            on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"order of {self.product.title}"

    def get_cost(self):
        return self.price*self.quantity
