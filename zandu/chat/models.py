from django.db import models
from django.conf import settings

class Message(models.Model):
    content=models.TextField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL, 
        related_name='author', on_delete=models.CASCADE)
    sent_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"message of {author.username}"