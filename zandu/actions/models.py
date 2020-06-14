from django.db import models

# Create your models here.
class Notification(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='notifcations',
                            db_index=True,
                            null=True,
                            blank=True,
                            on_delete=models.CASCADE)

    verb=models.CharField(max_length=250)
    target_ct=models.ForeignKey(ContentType, blank=True,
                                null=True, related_name='target',
                                on_delete=models.CASACDE)
    target_id=models.PositiveIntegerField(null=True, blank=True)
    target=GenericForeignKey('target_ct', 'target_id')
    created=models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        orderindg=('-created')

    def __str__(self):
        return f'{user}{verb}'    
