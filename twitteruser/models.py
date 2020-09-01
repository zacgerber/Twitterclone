from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class TwitUser(AbstractUser):
    displayname = models.CharField(max_length=80)
    age = models.IntegerField(null=True)
    bio = models.TextField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)

    REQUIRED_FIELDS = ['age', 'homepage']

    def __str__(self):
        return self.username
