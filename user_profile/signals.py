"""Imports for signals file"""
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from developer.models import DeveloperProfile
from .models import Profile

# pylint: disable=locally-disabled, no-member
# pylint: disable=unused-argument
# pylint: disable=unused-variable

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a user profile when a new user is created.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Save the user profile whenever the associated User object is saved.
    """
    instance.profile.save()


@receiver(post_save, sender=Profile)
def create_or_update_developer_profile(sender, instance, created, **kwargs):
    """Signal to create or delete DeveloperProfile based on is_developer flag
        If is_developer is False, delete the associated DeveloperProfile (if exists)
        """
    if instance.is_developer:
        developer_profile, created = DeveloperProfile.objects.get_or_create(
    user=instance.user,
    profile=instance
)
    else:
        DeveloperProfile.objects.filter(user=instance.user).delete()
