"""Imports for Admin page"""
from django.contrib import admin
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin
from .models import Profile, Category, Comment, Post

admin.site.register(Category)
admin.site.register(Comment)


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
    model = User, Profile
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class PostAdmin(SummernoteModelAdmin):
    """
    Allows admin to manage posts via the admin panel
    """
    list_display = ("title", "slug", "created_on", "status")
    search_fields = ["title", "content"]
    list_filter = ("created_on", "category")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)
    actions = ["approve_posts"]

    def approve_posts(self, _request, queryset):
        """
        Custom admin action to approve posts.
        """
        queryset.update(status=1)
    approve_posts.short_description = "Approve selected posts"


admin.site.register(Post, PostAdmin)
