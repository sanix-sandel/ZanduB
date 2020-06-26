from django.contrib import admin
from .models import (
    Product,
    ProductImage,
    ProductComment,
    Category
)

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductComment)
admin.site.register(Category)

admin.site.index_template='memcache_status/admin_index.html'
