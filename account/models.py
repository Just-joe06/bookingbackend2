from django.db import models
from .custom import customizeUser
from django.contrib.auth.models import AbstractUser
# Create your models here.


# Create your models here.

class User(AbstractUser):
    username = None
    photo = models.ImageField(upload_to="profile")
    email = models.EmailField(unique=True)
    objects = customizeUser()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []