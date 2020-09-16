from django.shortcuts import render, HttpResponseRedirect, reverse
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
# from django.contrib.auth import login

from tweet.models import TweetModel
from tweet.forms import TweetForm
from twitteruser.models import TwitUser
from notification.models import Notification
from django.views.generic.base import View
# from django.views.contribn.auth.mixins import LoginRequiredMixin
import re

# Create your views here.


# @login_required
# def create_tweet_view(request):
#     if request.method == "POST":
#         form = TweetForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             tweetpost = TweetModel.objects.create(
#                 body=data['body'],
#                 author=request.user,
#             )
#             if "@" in data['body']:
#                 recipients = re.findall(r'@(\w+)', data.get('body'))
#                 for recipient in recipients:
#                     match_user = TwitUser.objects.get(username=recipient)
#                     if match_user:
#                         message = Notification.objects.create(
#                             message_content=tweetpost, receiver=match_user)
#             return HttpResponseRedirect(reverse("homepage"))

#     form = TweetForm()
#     return render(request, 'base.html', {"form": form})

# @login_required
class create_tweet_view(LoginRequiredMixin, TemplateView):
    def get(self, request):
        form = TweetForm()
        return render(request, 'base.html', {"form": form})

    def post(self, request):
        if request.method == 'POST':
            form = TweetForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                tweetpost = TweetModel.objects.create(
                    body=data('body'),
                    author=request.user,
                )
                if "@" in data['body']:
                    recipients = re.findall(r'@(\w+)', data.get('body'))
                    for recipient in recipients:
                        match_user = TwitUser.objects.get(username=recipient)
                        if match_user:
                            message = Notification.objects.create(
                                message_content=tweetpost, receiver=match_user)
                return HttpResponseRedirect(reverse("homepage"))
            else:
                return render(request, self.html, {"form": form})


# def tweet_detail_view(request, tweet_id):
#     html = "tweet_detail.html"
#     tweet_detail = TweetModel.objects.filter(id=tweet_id).first()
#     return render(request, html, {"tweet": tweet_detail})


class tweet_detail_view(View):
    def get(self, request, tweet_id):
        html = "tweet_detail.html"
        tweet_detail = TweetModel.objects.filter(id=tweet_id).first()
        return render(request, html, {"tweet": tweet_detail})
