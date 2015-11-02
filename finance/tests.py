from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase

from accounts.factories import UserFactory


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
        self.assertRedirects(response, reverse('receipt_list'))
