
""" Admin Site settings"""
from django.contrib import admin
from .models import Contact, DeveloperProfile

admin.site.register(Contact)
admin.site.register(DeveloperProfile)
