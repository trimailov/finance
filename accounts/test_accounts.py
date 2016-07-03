from django.contrib.auth.models import User
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


class SignUpTests(TestCase):
    def test_sign_up_get(self):
        c = Client()
        response = c.get(reverse('registration_register'))
        self.assertEqual(200, response.status_code)

    def test_sign_up_post(self):
        c = Client()
        response = c.post(
            reverse('registration_register'),
            {'username': 'Anatolijus',
             'email': 'anatolka@example.com',
             'password1': 'secret',
             'password2': 'secret'},
            follow=True
        )
        self.assertRedirects(response, reverse('transaction_list'))

        self.assertTrue(User.objects.get(username='Anatolijus',
                                         is_active=True))
