from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("L'adresse email est obligatoire")
        user=self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password=None):
        user=self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)

        return user
