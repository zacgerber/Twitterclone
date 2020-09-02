from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class TwitAuthorModel(models.Model):
    name = models.CharField(max_length=80)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TweetModel(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField(max_length=140)
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(TwitAuthorModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.author.name}"
