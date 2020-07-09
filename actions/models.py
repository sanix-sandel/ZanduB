from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
import uuid
# Create your models here.
class Notification(models.Model):
    id=models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False
    )
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='notifcations',
                            db_index=True,
                            null=True,
                            blank=True,
                            on_delete=models.CASCADE)

    verb=models.CharField(max_length=250)
    target_ct=models.ForeignKey(ContentType, blank=True,
                                null=True, related_name='target',
                                on_delete=models.CASCADE)
    
    target_id=models.UUIDField(null=False, blank=False,
                                        db_index=True)
    target=GenericForeignKey('target_ct', 'target_id')
    created=models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering=('-created',)

    def __str__(self):
        return f'{self.user}  {self.verb}'    
