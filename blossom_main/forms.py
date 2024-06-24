"""Imports for Forms page"""
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post


class InsightForm(forms.ModelForm):
    """
    Form for creating and updating a Post.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        STATUS_CHOICES = [
            choice for choice in self.fields['status'].choices
            if choice[0] in (0, 2)
        ]
        self.fields['status'].choices = STATUS_CHOICES

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
