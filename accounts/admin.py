from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import account


class AccountAdmin(UserAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'username',
        'last_login',
        'is_active',
        'date_joined'
    )

    ordering = ('email',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(account, AccountAdmin)