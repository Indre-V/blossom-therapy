"""Imports for Models page"""
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# pylint: disable=unused-argument
# pylint: disable=locally-disabled, no-member


class Category(models.Model):
    """
    Model representing a category for the posts.
    """
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        """
        Options for Category model
        """
        verbose_name_plural = "Categories"

    def __str__(self):
        """
        String for representing the Model object
        """
        return f"{self.name}"

class Post(models.Model):
    """
    Model representing a blog post.
    """
    STATUS_CHOICES = (
        (0, 'Ready to Publish'),
        (1, 'Published'),
        (2, 'Save for Later')
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    featured_image = CloudinaryField('image', default='placeholder_insights')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    excerpt = models.TextField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="track_likes", blank=True)
    favourite = models.ManyToManyField(User, related_name="track_favs", blank=True)
    comment_count = models.IntegerField(default=0)

    class Meta:
        """
        Meta options for the Post model.
        """
        ordering = ["-created_on"]

    def count_likes(self):
        """
        Returns number of post likes
        """
        return self.likes.count()

    def count_favs(self):
        """
        Returns number of post likes
        """
        return self.favourite.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String for representing the Model object
        """
        return f"{self.title}"


class Comment(models.Model):
    """
    Model representing a comment on a post.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta options for the Comment model.
        """
        ordering = ["created_on"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return f'Comment by {self.author} on {self.post}'
