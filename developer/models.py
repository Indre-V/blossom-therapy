from django.db import models



class Contact(models.Model):
    """
    Contact form model
    """
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

