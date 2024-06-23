"""Imports for Admin page"""
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    """
    Inline for Profile model in UserAdmin.
    """
    model = Profile


class UserAdmin(admin.ModelAdmin):
    """
    Custom configuration for admin to update
    user profiles
    """
    model = Profile, User
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
