from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin

class ProfileInline(admin.StackedInline):
    """
    Inline for Profile model in UserAdmin.
    """
    model = Profile

class UserAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the User model.
    """
    model = User, Profile
    fields = ("username", "email")
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
