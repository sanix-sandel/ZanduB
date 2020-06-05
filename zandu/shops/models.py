from django.db import models
from django.conf import settings

class Store(models.Model):
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='store',
                            on_delete=models.CASACDE)

    image=models.ImageField(upload_to='store_pics/', blank=True)
    title=models.CharField(max_length=50)
    slogan=models.TextField()
    about=models.TextField()
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
