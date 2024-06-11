"""Imports for Admin page"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Comment, Post

admin.site.register(Category)
admin.site.register(Comment)


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
        queryset.filter(status=0).update(status=1)
    approve_posts.short_description = "Approve selected posts"

admin.site.register(Post, PostAdmin)
