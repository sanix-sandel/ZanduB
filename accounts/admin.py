from django.contrib import admin
from .models import User

#admin.site.index_template='memcache_status/admin_index.html'

admin.site.register(User)
