from django import forms
from twitteruser import models


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


# class AuthorForm(forms.ModelForm):
#     username = forms.CharField(max_length=240)
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = TwitUser
#         fields = ["name"]


class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.TwitUser
        fields = ['displayname', 'age']
