"""Imports for Admin page"""
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    """
    Inline for Profile model in UserAdmin.
    """
    model = Profile
    exclude = ['total_likes', 'total_favourites']
    can_delete = False


class UserAdmin(admin.ModelAdmin):
    """
    Custom configuration for admin to update
    user profiles
    """
    model = User, Profile
    inlines = [ProfileInline]

    list_display = ['username', 'date_joined', 'last_login', 'is_superuser']
    search_fields = ['username', 'first_name', 'last_name']
    exclude = ['groups', 'user_permissions', 'is_staff']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
