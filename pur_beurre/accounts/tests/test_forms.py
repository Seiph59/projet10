from django.test import TestCase,Client
from accounts.forms import UserRegisterForm
from django.contrib.auth.models import User

# Create your tests here.
class FormTest(TestCase):
    def setUp(self):
        self.data = {'username': 'seiph', 'first_name': 'Jean',
        'last_name':'Robert', 'email':'jbr@aol.com',
        'password1': 'kevin1234', 'password2': 'kevin1234'}

    def test_valid_form_true(self):
        form = UserRegisterForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_valid_form_false(self):
        form = UserRegisterForm(data={'username': 'seiph'})
        self.assertFalse(form.is_valid())

    def test_error_user_already_exists(self):
        User.objects.create_user(username="test", first_name="Al",
        last_name="taga", email="albg@sfr.fr", password="kevin1234")
        client = Client()
        client.post('/register/', {'username': 'test', 'first_name': 'Jean',
        'last_name':'Robert', 'email':'jbr@aol.com',
        'password1': 'kevin1234', 'password2': 'kevin1234'})
        self.assertRaisesMessage(ValueError, 'user already exists')
