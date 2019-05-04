from django.test import TestCase, Client
from django.urls import resolve, reverse
from welcome.views import index

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

class TestViewsWelcome(TestCase):

    def test_welcome_get(self):
        client = Client()
        response = client.get(reverse('welcome:home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome/index.html')
# Create your tests here.
