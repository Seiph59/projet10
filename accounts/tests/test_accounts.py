""" Test file about accounts """

from django.test import TestCase, Client
from django.contrib.auth.models import User


class UserAccountTest(TestCase):
    """ Test about User account, database, creation """

    def test_no_account_db(self):
        """ Check if basically, there is no account in db """
        count_accounts = User.objects.count()
        self.assertEqual(count_accounts, 0)

    def test_new_user_account_created(self):
        """ Check if the User account creation works """
        accounts_before = User.objects.count()
        self.assertEqual(accounts_before, 0)
        User.objects.create_user(username="test",
                                 first_name="Al",
                                 last_name="taga",
                                 email="albg@sfr.fr",
                                 password="kevin1234")
        accounts_after = User.objects.count()
        self.assertEqual(accounts_after, 1)

    def test_account_created_by_client(self):
        """ Check if create an account from Client works """
        accounts_before = User.objects.count()
        self.assertEqual(accounts_before, 0)
        client = Client()
        client.post('/register/', {'username': 'seiph',
                                   'first_name': 'Jean',
                                   'last_name': 'Robert',
                                   'email': 'jbr@aol.com',
                                   'password1': 'kevin1234',
                                   'password2': 'kevin1234'})
        account_check = User.objects.count()
        self.assertEqual(account_check, 1)
