""" Test file dedicated to urls.py file """

from django.test import TestCase
from django.urls import resolve
from accounts.views import register, my_account


class AccountsTest(TestCase):
    """ Class for urls tests """

    def test_register_url_resolves_to_register_view(self):
        """ test if the url is well associated to register view """
        found = resolve('/register/')
        self.assertEqual(found.func, register)

    def test_myaccount_url_resolves_to_my_account_view(self):
        """ test if the url is well associated to my_account view """
        found = resolve('/myaccount/')
        self.assertEqual(found.func, my_account)
