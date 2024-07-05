"""Apps imports"""
from django.apps import AppConfig

# pylint: disable=unused-import
# pylint: disable=import-outside-toplevel

class UserProfileConfig(AppConfig):
    """
    Default Django
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profile'

    def ready(self):
        import user_profile.signals
