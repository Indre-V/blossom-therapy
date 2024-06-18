"""Developer models imports"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


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
    Developer profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    image = CloudinaryField('image', blank=True)
    resume_download_link = models.URLField(max_length=255, blank=True)
    github_portfolio_link = models.URLField(max_length=255, blank=True)
    linkedin_profile_link = models.URLField(max_length=255, blank=True)
    skills = models.TextField(blank=True)
    languages = models.TextField(blank=True)
    education = models.TextField(blank=True)
    certifications = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
