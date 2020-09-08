"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from django.conf.urls import patterns, url

from twitteruser.views import signup_view, user_detail_view, index, follow_view, unfollow_view, SignUpView, UnfollowView, followView
from authentication.views import login_view, logout_view
from tweet.views import create_tweet_view, tweet_detail_view, TweetDetailView, CreateTweet
from notification.views import notification_view

urlpatterns = [
    path('', index, name='homepage'),
    path('create_tweet_view/', create_tweet_view, name="createtweet"),
    path('altcreatetweet', CreateTweet.as_view()),
    path('tweet_detail_view/<int:tweet_id>/', tweet_detail_view, name="tweetdetail"),
    path('alttweetdetailview/<int:tweet_id>/', TweetDetailView.as_view()),
    path('user_detail_view/<int:tweet_id>/', user_detail_view, name="userdetail"),
    path('notification_view/', notification_view, name="notification"),
    path('login_view/', login_view, name='login'),
    path('signup_view/', signup_view, name='signup'),
    path('altsignupview/', SignUpView.as_view()),
    path('logout_view/', logout_view, name="logout"),
    path('follow_view/<int:follow_id>/', follow_view, name="follow"),
    path('altfollowview/<int:follow_id>/', followView.as_view()),
    path('unfollow_view/<int:unfollow_id>/', unfollow_view, name="unfollow"),
    path('altunfollowview/<int:unfollow_id>/', UnfollowView.as_view()),
    path('admin/', admin.site.urls),
]
