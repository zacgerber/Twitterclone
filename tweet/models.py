from django.db import models
from django.utils import timezone
from twitteruser.models import TwitUser
# Create your models here.


class TweetModel(models.Model):
    body = models.TextField(max_length=140)
    post_date = models.DateTimeField(default=timezone.now, editable=False)
    author = models.ForeignKey(TwitUser, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post_date} - {self.author}"
