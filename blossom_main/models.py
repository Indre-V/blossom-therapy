from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """
    A model representing a user profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = CloudinaryField('image', default='placeholder_profile')
    location = models.CharField(max_length=255, blank=True)
    total_likes = models.IntegerField(default=0)
    total_favourites = models.IntegerField(default=0)

    def __str__(self):
        """
        Return the string representation of the associated user's first name if it exists
        """
        return f"{self.first_name} {self.last_name}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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
        (0, 'Draft'),
        (1, 'Published')
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='placeholder_insights')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    excerpt = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes_count = models.IntegerField(default=0)
    favourites_count = models.IntegerField(default=0)

    class Meta:
        """
        Meta options for the Post model.
        """
        ordering = ["-created_on"]

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
  