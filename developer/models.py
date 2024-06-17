"""Developer models imports"""
from django.db import models
from django.contrib.auth.models import User
from user_profile.models import Profile

# pylint: disable=locally-disabled, no-member

class Contact(models.Model):
    """
    Contact form model
    """
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15, blank=True, null=True)  
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) 

    def __str__(self):

        return f"{self.email} - {self.created_on}"

class DeveloperProfile(models.Model):
    """
    Model representing a developer profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    resume_download_link = models.URLField(max_length=255, blank=True)
    github_portfolio_link = models.URLField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'Developer Profile'
        verbose_name_plural = 'Developer Profiles'

    def __str__(self):
        return str(self.user.username)
