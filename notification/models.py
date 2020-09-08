from django.db import models
from tweet.models import TweetModel
from twitteruser.models import TwitUser
# Create your models here.


class Notification(models.Model):
    receiver = models.ForeignKey(
        TwitUser, related_name="receiver", on_delete=models.CASCADE,
        blank=True, null=True)
    message_content = models.ForeignKey(
        TweetModel, blank=True, null=True, on_delete=models.CASCADE)
    notification_flag = models.BooleanField(default=False)
