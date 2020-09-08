from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class TwitUser(AbstractUser):
    displayname = models.CharField(max_length=80, null=True)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.username
