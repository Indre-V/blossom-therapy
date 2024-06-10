"""Imports for Forms page"""
from django import forms
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.models import User
from .models import Profile, Comment, Post


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
            "bio",
            "profile_picture",
            "location",
        ]
        widgets = {
            "profile_picture": forms.FileInput(),
        }


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
            "username",
            "first_name",
            "last_name",
            "email",
        ]

    username = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=40)


class InsightForm(forms.ModelForm):
    """
    Form for creating and updating a Post.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['excerpt'].widget = forms.Textarea(attrs={'rows': 2})
        self.fields['content'].widget = SummernoteWidget(attrs={'rows': 5})

    class Meta:
        """
        Meta options for the PostForm.
        Specifies the model to use and the fields to include in the form.
        """
        model = Post
        fields = ['title', 'featured_image','excerpt', 'content', 'category']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
            'excerpt': forms.Textarea(attrs={'rows': 2}),
        }
        labels = {
            'title': 'Title',
            'category': 'Category',
            'featured_image': 'Featured Image',
            'excerpt': 'Excerpt',
            'content': 'Content',
            'status': 'Status',

        }
        widgets = {
            'content': SummernoteWidget(),
            'excerpt': SummernoteWidget(),
        }


class CommentForm(forms.ModelForm):
    """
    A form for creating and updating comments on a blog post.
    """
    class Meta:
        """
        Meta options for the CommentForm.
        Specifies the model to use and the fields to include in the form.
        """
        model = Comment
        fields = ['content']
