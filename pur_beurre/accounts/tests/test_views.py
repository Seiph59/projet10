from django.test import TestCase, Client
from django.contrib.auth.models import User


class RedirectTest(TestCase):

    def test_redirect_if__try_access_myaccount_without_login(self):
        response = self.client.get('/myaccount/')
        self.assertEqual(response.status_code, 302)

    def test_redirect_when_account_created_to_homepage(self):
        response = self.client.post('/register/', {'username': 'seiph', 'first_name': 'Jean',
        'last_name':'Robert', 'email':'jbr@aol.com',
        'password1': 'kevin1234', 'password2': 'kevin1234'})
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('welcome/index.html')

    def test_redirect_when_login_to_homepage(self):
        User.objects.create_user(username="test", first_name="Al",
        last_name="taga", email="albg@sfr.fr", password="kevin1234")
        response = self.client.post('/login/', {'username': 'test', 'password':'kevin1234'})
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('welcome/index.html')