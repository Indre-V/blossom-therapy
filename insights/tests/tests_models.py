"""Imports for Model Testing"""
import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from insights.models import Category, Post, Comment

# pylint: disable=locally-disabled, no-member


class CategoryModelTest(TestCase):
    """
    Category Model testing
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified data for all class methods.
        """
        Category.objects.create(name='Test Category')

    def test_get_absolute_url(self):
        """
        Test for verifying the get_absolute_url method of the Category model.
        """
        category = Category.objects.get(id=1)
        self.assertEqual(category.get_absolute_url(), '/insights/')


class PostModelTest(TestCase):
    """
    Post model testing
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified data for all class methods.
        """
        author = User.objects.create(username='testuser')
        category = Category.objects.create(name='Test Category')
        Post.objects.create(
            title='Test Post', slug='test-post',
            author=author, content='Test content', category=category
        )

    def test_str_representation(self):
        """
        Test for verifying the string representation of the Post model.
        """
        post = Post.objects.get(id=1)
        self.assertEqual(str(post), 'Test Post')

    def test_count_likes(self):
        """
        Test for verifying the count_likes method of the Post model.
        """
        post = Post.objects.get(id=1)
        self.assertEqual(post.count_likes(), 0)

    def test_count_favs(self):
        """
        Test for verifying the count_favs method of the Post model.
        """
        post = Post.objects.get(id=1)
        self.assertEqual(post.count_favs(), 0)


class CommentModelTest(TestCase):
    """
    Comment Model testing
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified data for all class methods.
        """
        author = User.objects.create(username='testuser')
        category = Category.objects.create(name='Test Category')
        post = Post.objects.create(
            title='Test Post', slug='test-post',
            author=author, content='Test content', category=category
        )
        Comment.objects.create(
            post=post, author=author,
            content='Test comment', approved=False
        )

    def test_approved_default_value(self):
        """
        Test for verifying the default value of the approved field.
        """
        comment = Comment.objects.get(id=1)
        self.assertFalse(comment.approved)

    def test_str_representation(self):
        """
        Test for verifying the string representation of the Comment model.
        """
        comment = Comment.objects.get(id=1)
        self.assertEqual(str(comment), 'Comment by testuser on Test Post')


if __name__ == '__main__':
    unittest.main()
