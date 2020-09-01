from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from twitteruser.models import TwitUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading (extra credit)',
            {
                'fields': (
                    'age',
                    'displayname',
                    'homepage',
                )
            }
        )
    )


admin.site.register(TwitUser, CustomUserAdmin)
