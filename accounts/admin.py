from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserAccount


class StyleUser(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_admin', 'is_active')
    list_display_links = ('username', 'email')
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(UserAccount, StyleUser)