"""Imports for Forms page"""
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post


class InsightForm(forms.ModelForm):
    """
    Form for creating and updating a Post.
    """
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user_is_admin():
            self.fields['status'].choices = Post.STATUS_CHOICES
        else:
            self.fields['status'].choices = [
                choice for choice in Post.STATUS_CHOICES
                if choice[0] in (0, 2)
            ]

    def user_is_admin(self):
        """
        Helper method to check if the user is an admin.
        You can customize this method based on your user model or permissions.
        """
        return self.user and self.user.is_superuser

    class Meta:
        """
        Meta options for the PostForm.
        Specifies the model to use and the fields to include in the form.
        """
        model = Post
        fields = ['title', 'featured_image', 'content', 'category', 'status']
        widgets = {
            'content': SummernoteWidget(attrs={'rows': 5}),
        }
        labels = {
            'title': 'Title',
            'category': 'Category',
            'featured_image': 'Featured Image',
            'content': 'Content',
            'status': 'Status',
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
