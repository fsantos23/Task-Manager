from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CreateUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

