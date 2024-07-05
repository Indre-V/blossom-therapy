"""Imports for Admin page"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Comment, Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Allows admin to manage posts via the admin panel
    """
    list_display = ['title', 'created_on', 'status', 'author']
    search_fields = ['title', 'content', 'author']
    list_filter = ['created_on', 'category']
    exclude = ['likes', 'favourite', 'comment_count']
    summernote_fields = ('content',)
    actions = ['approve_posts']

    def get_queryset(self, request):
        """
        Customize the queryset to display only records with status 0 or 1.
        """
        queryset = super().get_queryset(request)
        return queryset.filter(status__in=[0, 1])

    def approve_posts(self, _request, queryset):
        """
        Custom admin action to approve posts.
        """
        queryset.filter(status=0).update(status=1)
    approve_posts.short_description = 'Approve selected insights'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Allows admin to manage comments on insights via the admin panel"""
    list_display = ['author', 'content', 'created_on']
    list_filter = ('created_on',)
    search_fields = ['author', 'content']


admin.site.register(Category)
