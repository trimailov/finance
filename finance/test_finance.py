from django.contrib.auth.models import User
from django.core.management import call_command
from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase

from accounts.factories import UserFactory
from books.models import Transaction


class HomePageTests(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_home_not_logged_in(self):
        c = Client()
        response = c.get(reverse('home'))
        self.assertEqual(200, response.status_code)

    def test_home_logged_in(self):
        c = Client()
        logged_in = c.login(username=self.user.username, password='secret')
        self.assertTrue(logged_in)

        response = c.get(reverse('home'))
        self.assertRedirects(response, reverse('transaction_list'))


class PopulateTests(TestCase):
    def test_populate_command(self):
        call_command('populate')
        self.assertTrue(User.objects.get(username='admin'))
        self.assertEqual(Transaction.objects.count(), 20)

        # test if no error is raised if ran 2nd time
        call_command('populate')
        self.assertTrue(User.objects.get(username='admin'))
        self.assertEqual(Transaction.objects.count(), 40)
