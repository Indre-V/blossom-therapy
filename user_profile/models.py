
""" User Profile Imports"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# pylint: disable=unused-argument
# pylint: disable=locally-disabled, no-member

class Profile(models.Model):
    """
    A model representing a user profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=150, blank=True)
    profile_picture = CloudinaryField('image', default='placeholder_profile')
    location = models.CharField(max_length=255, blank=True)
    total_likes = models.IntegerField(default=0)
    total_favourites = models.IntegerField(default=0)

