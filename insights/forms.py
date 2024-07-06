"""Imports for Forms page"""
from django import forms
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post

# pylint: disable=locally-disabled, no-member


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

    def clean_title(self):
        """
        Custom validation to check
        if a post with the same title already exists.
        """
        title = self.cleaned_data.get('title')
        slug = slugify(title)

        if Post.objects.filter(slug=slug).exclude(pk=self.instance.pk).exists():
            raise ValidationError('A post with this title already exists.')
        return title

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


class CommentForm(forms.ModelForm):
    """
    A form for creating and updating comments on a blog post.
    """
    content = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={
            'rows': 5,
            'cols': 30
        })
    )

    class Meta:
        """
        Meta options for the CommentForm.
        Specifies the model to use and the fields to include in the form.
        """
        model = Comment
        fields = ['content']
