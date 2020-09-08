from django import forms
from tweet.models import TweetModel


class TweetForm(forms.ModelForm):

    class Meta:
        model = TweetModel
        fields = ['body']
