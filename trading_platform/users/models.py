from django.db import models
from django.contrib.auth.models import AbstractUser

from users.manager import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    date_of_birth = models.DateField('date of birth')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    