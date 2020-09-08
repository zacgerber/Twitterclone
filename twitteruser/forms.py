from django import forms
from twitteruser import models


class SignupForm(forms.ModelForm):
    displayname = forms.CharField(max_length=50)
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.TwitUser
        fields = ['displayname']
