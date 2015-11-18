from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase

from accounts.factories import UserFactory


class LoginTests(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_login_get(self):
        c = Client()
        response = c.get(reverse('login'))
        self.assertEqual(200, response.status_code)

    def test_login_post(self):
        c = Client()
        response = c.post(
            reverse('login'),
            {'username': self.user.username, 'password': 'secret'},
            follow=True
        )
        self.assertRedirects(response, reverse('transaction_list'))

    def test_login_and_remember_post(self):
        c = Client()
        response = c.post(
            reverse('login'),
            {'username': self.user.username,
             'password': 'secret',
             'remember_me': 'on'},
            follow=True
        )
        self.assertRedirects(response, reverse('transaction_list'))

    def test_login_redirect(self):
        c = Client()
        logged_in = c.login(username=self.user.username, password='secret')
        self.assertTrue(logged_in)

        response = c.get(reverse('login_redirect'))
        self.assertRedirects(response, reverse('transaction_list'))
