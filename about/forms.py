"""Imports for Forms page"""
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """Create Contact Form"""
    class Meta:
        """Get Contact model,  display fields"""
        model = Contact
        fields = '__all__'
