"""Imports for Forms page"""
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class ProfileForm(forms.ModelForm):
    """
    User profile page form
    """

    class Meta:
        """
        Form fields
        """

        model = Profile
        fields = [
            'bio',
            'profile_picture',
            'location'
        ]


class UserForm(forms.ModelForm):
    """
    Form for user registration and profile information
    """
    class Meta:
        """
        Form fields
        """

        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
        ]

    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=40)
