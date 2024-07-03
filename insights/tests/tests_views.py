from django.test import TestCase, Client
from django.contrib.auth.models import User
from insights.models import Post, Category
from insights.views import InsightUpdateView
from django.contrib.messages import get_messages
from django.urls import reverse

# pylint: disable=locally-disabled, no-member

class TestHomeView(TestCase):
    """
    Test suite for the HomeView in the insights app.
    """

    def setUp(self):
        """
        Set up the test client
        """
        self.client = Client()
        self.url = reverse('home')

    def test_home_view(self):
        """
        Test the HomeView for proper status code, template used,
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

class InsightDetailsViewTestCase(TestCase):
    """
    Test case for testing InsightDetailsView behavior.
    """

    def setUp(self):
        """
        Set up the necessary data for each test.
        """
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='Test Category')
        self.post = Post.objects.create(
            title='Test Post', content='Test content', author=self.user, category=self.category)
        self.url = reverse('insight-details', kwargs={'slug': self.post.slug})

    def test_post_request(self):
        """
        Test the behavior of the insight details view when submitting a comment via POST request.
        """
        self.client.force_login(self.user)
        comment_data = {
            'content': 'Test comment content'
        }
        response = self.client.post(self.url, comment_data)
        self.assertEqual(response.status_code, 302)


class SearchViewTestCase(TestCase):
    """
    Test cases for the SearchView class-based view.
    """

    def setUp(self):
        """
        Set up the necessary URL for testing.
        """
        self.url = reverse('search')

    def test_get_request(self):
        """
        Test the GET request to the search view.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'insights/search-results.html')

    def test_filtered_queryset(self):
        """
        Test the GET request to the search view with a query string.
        """
        response = self.client.get(self.url + '?q=test')  # Example with a search query
        self.assertEqual(response.status_code, 200)

class InsightDeleteViewTestCase(TestCase):
    """
    Test case for testing the deletion of a Post using the InsightDeleteView.
    """

    def setUp(self):
        """
        Set up the test environment by creating necessary objects and URLs.
        """
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(self.user)

        self.category = Category.objects.create(name='Test Category')

        self.post = Post.objects.create(
            title='Test Post',
            content='Test content',
            author=self.user,
            category=self.category
        )

        self.url = reverse('insight-delete', kwargs={'slug': self.post.slug})

    def test_delete_post(self):
        """
        Test case to verify the deletion of a post by an authorized user.
        """
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

    def test_unauthorized_user(self):
        """
        Test case to verify that an unauthorized user cannot delete the post.
        """
        another_user = User.objects.create_user(username='anotheruser', password='12345')
        self.client.force_login(another_user)

        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 403)
        self.assertTrue(Post.objects.filter(pk=self.post.pk).exists())

class InsightUpdateViewTestCase(TestCase):
    """
    Update View Tests
    """
    def setUp(self):
        """
        Set up the necessary data for the test case.
        """
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

        self.category = Category.objects.create(name='General')
        self.insight = Post.objects.create(
            title='Test Insight',
            content='Test content',
            category=self.category,  # Assign the Category instance
            author=self.user
        )

        self.url = reverse('insight-update', kwargs={'slug': self.insight.slug})
        self.new_title = 'Updated Insight'

    def test_update_insight_unauthorized(self):
        """
        Test that unauthorized users cannot update an insight.
        """
        self.client.logout()

        response = self.client.post(self.url, {
            'title': self.new_title,
            'content': 'Updated content',
            'category': self.category.id
        })

        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

        updated_insight = Post.objects.get(pk=self.insight.pk)
        self.assertNotEqual(updated_insight.title, self.new_title)

class InsightAddViewTestCase(TestCase):
    """
    Test case for InsightAddView class-based view.
    """

    def setUp(self):
        """
        Set up the necessary data for the test case.
        """
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

        self.category = Category.objects.create(name='General')

        self.url = reverse('add-insight')

        self.new_insight_data = {
            'title': 'New Insight',
            'content': 'New insight content',
            'category': self.category.id,
            'status': 1 
        }

    def test_insight_add_view(self):
        """
        Testing Inside add functionality
        """
        url = reverse('add-insight')
        data = {
            'title': '',  
            'content': 'New insight content',
            'category': 1,  
            'status': 1,  
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')

    def test_insight_add_view_invalid_form(self):
        """
        Test case to verify handling of invalid form data.
        """
        invalid_data = self.new_insight_data.copy()
        invalid_data['title'] = ''  # Simulate an invalid form field

        response = self.client.post(self.url, invalid_data, follow=True)
        print(response.status_code)
        print(response.content)  # Print response content for debugging

        self.assertEqual(response.status_code, 200)

        self.assertFalse(Post.objects.filter(title=self.new_insight_data['title']).exists())

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Try Again. Please check all fields.')
