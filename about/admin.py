""" Admin Site Imports"""
from django.contrib import admin
from .models import Contact, DevProfile


admin.site.register(DevProfile)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Allows admin to manage user contacts via the admin panel"""
    list_display = ['email', 'subject', 'created_on']
