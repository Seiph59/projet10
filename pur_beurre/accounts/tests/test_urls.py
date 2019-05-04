from django.test import TestCase
from django.urls import resolve
from accounts.views import register, my_account

class AccountsTest(TestCase):

    def test_register_url_resolves_to_register_view(self):
        found = resolve('/register/')
        self.assertEqual(found.func, register)

    def test_myaccount_url_resolves_to_my_account_view(self):
        found = resolve('/myaccount/')
        self.assertEqual(found.func, my_account)

