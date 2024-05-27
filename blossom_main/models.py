from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """
    A model representing a user profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = CloudinaryField('image', default='placeholder_profile')
    location = models.CharField(max_length=255, blank=True)
    total_likes = models.IntegerField(default=0)
    total_favourites = models.IntegerField(default=0)

    def __str__(self):
        """
        Return the string representation of the associated user's first name if it exists
        """
        return f"{self.first_name} {self.last_name}"
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()