from django import forms
from tweet.models import TweetModel


class TweetForm(forms.Form):
    title = forms.CharField(max_length=80)
    body = forms.CharField(widget=forms.Textarea)
