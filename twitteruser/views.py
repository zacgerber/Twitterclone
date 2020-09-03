from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# from authentication.views import login_view
from twitteruser.models import TwitUser
from twitteruser.forms import SignupForm
from django.conf import settings

# from django.contrib.auth.models import User


@login_required
def index(request):
    return render(request, "index.html", {"display": settings.AUTH_USER_MODEL})


def author_detail(request, post_id):
    html = "author_detail.html"
    my_author = TwitUser.objects.filter(id=post_id).first()
    return render(request, html, {"post": my_author})


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
