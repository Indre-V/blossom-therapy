"""Imports for Form Testing"""
from django.test import TestCase
from django.contrib.auth.models import User
from insights.forms import InsightForm, CommentForm
from insights.models import Category


# pylint: disable=locally-disabled, no-member
class InsightFormValidationTests(TestCase):
    """
    Unit tests for validating InsightForm.
    """

    def setUp(self):
        """
        Set up the necessary data for the test case.
        """

        self.user = User.objects.create_user(username='testuser', password='password123')


        self.category = Category.objects.create(name='General')

    def test_valid_form_data(self):
        """
        Test case for validating form with valid data.
        """
        form_data = {
            'title': 'Test Insight',
            'featured_image': 'image.jpg',
            'content': 'Lorem ipsum content',
            'category': self.category.id,
            'status': 0,
        }

        form_data['user'] = self.user

        form = InsightForm(data=form_data)

        self.assertTrue(form.is_valid(), form.errors)

    def test_invalid_form_data(self):
        """
        Test case for validating form with invalid data.
        """
        form_data = {
            'title': '',  # Invalid empty title
            'featured_image': None,  # Invalid empty featured_image
            'content': 'Lorem ipsum content',
            'category': 999,  # Use an invalid category ID
            'status': 1,
        }

        form_data['user'] = self.user

        form = InsightForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors)

class CommentFormTests(TestCase):
    """
    Unit tests for validating CommentForm.
    """

    def test_valid_comment_form(self):
        """
        Test case for validating form with valid data.
        """
        form_data = {
            'content': 'This is a valid comment.',
        }

        form = CommentForm(data=form_data)

        self.assertTrue(form.is_valid(), form.errors)

    def test_empty_content_comment_form(self):
        """
        Test case for validating form with empty content.
        """
        form_data = {
            'content': '',
        }

        form = CommentForm(data=form_data)

        self.assertFalse(form.is_valid())


        self.assertIn('content', form.errors)

    def test_missing_content_comment_form(self):
        """
        Test case for validating form with missing content.
        """
        form_data = {}

        form = CommentForm(data=form_data)


        self.assertFalse(form.is_valid())


        self.assertIn('content', form.errors)
