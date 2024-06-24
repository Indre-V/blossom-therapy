
""" Admin Site settings"""
from django.contrib import admin
from .models import Contact, DevProfile

admin.site.register(Contact)
admin.site.register(DevProfile)
