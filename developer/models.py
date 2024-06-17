from django.db import models
from django.utils import timezone

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