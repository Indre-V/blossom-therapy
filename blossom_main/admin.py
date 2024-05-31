from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Category, Comment, Post
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

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)