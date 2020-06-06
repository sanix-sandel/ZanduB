from django.db import models
from django.contrib.auth.models AbstractBaseUser
from django.contrib.auth import get_user_model
from managers import UserManager
from django.conf import settings
from django.contrib.contentTypes.fields import GenericRelation


class User(AbstractBaseUser):
    username=models.CharField(max_length=50)
    email=models.EmailField(
        verbose_name='adresse_email',
        max_length=250,
        unique=True,
    )
    profile_image=models.ImageField(upload_to='profile_pics/', blank=True)
    #notif
    #groupe
    #location
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    reports=PositiveIntegerField()#for supspicious activity

    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
