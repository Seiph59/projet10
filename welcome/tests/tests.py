""" Test file for welcome Application """
from django.test import TestCase, Client
from django.urls import resolve, reverse
from welcome.views import index


class HomePageTest(TestCase):
    """ Class dedicated for Homepage tests """

    def test_root_url_resolves_to_home_page_view(self):
        """ Test if root works """
        found = resolve('/')
        self.assertEqual(found.func, index)


class TestViewsWelcome(TestCase):
    """ Class dedicated for views tests """
    def test_welcome_get(self):
        """ Method which test the GET method """
        client = Client()
        response = client.get(reverse('welcome:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome/index.html')
