"""Imports for Models page"""
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# pylint: disable=unused-argument
# pylint: disable=locally-disabled, no-member


class Profile(models.Model):
    """
    A model representing a user profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=150, blank=True)
    profile_picture = CloudinaryField('image', default='placeholder_profile')
    location = models.CharField(max_length=255, blank=True)
    total_likes = models.IntegerField(default=0)
    total_favourites = models.IntegerField(default=0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a user profile when a new user is created.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Save the user profile whenever the associated User object is saved.
    """
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
    likes_count = models.IntegerField(default=0)
    favourites_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

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


class Like(models.Model):
    """
    Model to represent a like on a post.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='likes', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta options for the Like model.
        """
        unique_together = ('user', 'post')

    def save(self, *args, **kwargs):
        # Check if the like instance already exists
        if self.pk is None:
            # New like, increase likes_count
            self.post.likes_count += 1
        else:
            # Existing like being updated or removed
            if self._state.adding:
                # New like being added
                self.post.likes_count += 1
            else:
                # Existing like being removed
                self.post.likes_count -= 1
        # Save the like instance
        super(Like, self).save(*args, **kwargs)
        # Save the associated post
        self.post.save()

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"


class Favourite(models.Model):
    """
    Model to represent a favourite post.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='favourites', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post)
