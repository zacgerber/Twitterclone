from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.contrib.auth.models import User
# Create your models here.


class TwitUser(AbstractUser):
    displayname = models.CharField(max_length=80)
    # username = models.CharField(max_length=80)

    def __str__(self):
        return self.username
