from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# from authentication.views import login_view
from twitteruser.models import TwitUser
from twitteruser.forms import SignupForm
from tweet.models import TweetModel
from notification.models import Notification

# from django.contrib.auth.models import User


@login_required
def index(request):
    html = 'index.html'
    recent_tweets = TweetModel.objects.filter(author=request.user)
    following_list = TweetModel.objects.filter(
        author__in=request.user.following.all())
    twitter_feed = recent_tweets | following_list
    twitter_feed = twitter_feed.order_by("-post_date")
    notifications = Notification.objects.filter(
        receiver__id=request.user.id, notification_flag=False)
    return render(request, html, {
        "tweets": recent_tweets, "following_list": following_list,
        "twitter_feed": twitter_feed, "notifications": notifications})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitUser.objects.create_user(
                displayname=data.get("displayname"),
                username=data.get("username"),
                password=data.get("password")
                )
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, 'base.html', {"form": form})


def user_detail_view(request, tweet_id):
    html = "user_detail.html"
    my_user = TwitUser.objects.filter(id=tweet_id).first()
    user_tweets = TweetModel.objects.filter(author=my_user)
    return render(request, html, {"tweets": user_tweets})


def follow_view(request, follow_id):
    signed_in_user = TwitUser.objects.get(username=request.user.username)
    add_user = TwitUser.objects.filter(id=follow_id).first()
    signed_in_user.following.add(add_user)
    signed_in_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def unfollow_view(request, unfollow_id):
    signed_in_user = TwitUser.objects.get(username=request.user.username)
    remove_user = TwitUser.objects.filter(id=unfollow_id).first()
    signed_in_user.following.add(remove_user)
    signed_in_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
