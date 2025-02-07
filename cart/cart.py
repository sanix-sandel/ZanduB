from decimal import Decimal
from django.conf import settings
from django.db import models
from products.models import Product

class Cart(object):

    def __init__(self, request, cart_id):

        self.session=request.session
        cart=self.session.get(cart_id)
        if not cart:
            cart=self.session[cart_id]={}
        self.cart=cart


    def add(self, product, quantity=1, override_quantity=False):

        product_id=str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':0,
                                    'price':str(product.price)}

        if override_quantity:
            self.cart[product_id]['quantity']=quantity
        else:
            self.cart[product_id]['quantity']+=quantity

        self.save()


    def save(self):
        self.session.modified=True


    def remove(self, product):

        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def __iter__(self):
        #This __iter__() method will allow you to easily
        #iterate over the items
        #in the cart in views and templates.
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)

        cart=self.cart.copy()
        for product in products:
            cart[str(product.id)]['product']=product

        for item in cart.values():
            item['price']=Decimal(item['price'])
            item['total_price']=item['price']*item['quantity']
            yield item


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item
                        in self.cart.values()
                    )

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
