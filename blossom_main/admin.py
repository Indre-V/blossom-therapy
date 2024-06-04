from django.contrib import admin
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin
from .models import Profile, Category, Comment, Post


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

class PostAdmin(admin.ModelAdmin):
    """
    Allows admin to manage posts via the admin panel
    """
    list_display = ("title", "slug", "created_on", "status")
    search_fields = ["title", "content"]
    list_filter = ("created_on", "category")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)
    actions = ["approve_posts"]

    def approve_posts(self, request, queryset):
        """
        Custom admin action to approve posts.
        """
        queryset.update(status=1)
    approve_posts.short_description = "Approve selected posts"

class CategoryAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)


admin.site.register(Comment, CommentAdmin)
