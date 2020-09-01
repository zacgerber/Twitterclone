from django.shortcuts import render, HttpResponseRedirect, reverse
# from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate, login, logout

from twitteruser.models import TwitUser
from twitteruser.forms import LoginForm, SignupForm
from django.conf import settings

# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User


def index(request):
    return render(request, "index.html", {"display": settings.AUTH_USER_MODEL})


def author_detail(request, post_id):
    html = "author_detail.html"
    my_author = TwitUser.objects.filter(id=post_id).first()
    return render(request, html, {"post": my_author})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                'username'), password=data.get("password"))
            if user:
                login(request, user)
                # return render(request, 'index.html', {"form": form})
                return HttpResponseRedirect(
                    request.GET.get('next', reverse("homepage")))

    form = LoginForm()
    return render(request, 'base.html', {"form": form})


# @login_required
# def author_form_view(request):
#     if request.user.is_staff:

#         if request.method == "POST":
#             form = AuthorForm(request.POST)
#             if form.is_valid():
#                 data = form.cleaned_data
#                 new_user = User.objects.create_user(username=data.get(
#                     "username"), password=data.get("password"))
#                 TwitUser.objects.create(name=data.get(
#                     "username"), user=new_user)
#                 return HttpResponseRedirect(reverse("homepage"))
#     else:
#         return HttpResponse("Dont have proper credentials return home")
#     form = AuthorForm()
#     return render(request, "basic_form.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
                displayname=data.get("displayname")
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()
    return render(request, 'base.html', {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
