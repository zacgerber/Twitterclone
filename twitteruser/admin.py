from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from twitteruser.models import TwitUser

# Register your models here.


admin.site.register(TwitUser, UserAdmin)
