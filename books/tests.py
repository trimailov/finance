from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase

from books.factories import TransactionFactory
from books.factories import UserFactory
from books.models import Transaction


class TransactionTests(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_create_model(self):
        self.assertEqual(0, Transaction.objects.count())
        TransactionFactory()
        self.assertEqual(1, Transaction.objects.count())
        self.assertEqual(str(Transaction.objects.latest('id')),
                         'transaction_0')

    def test_transaction_create_get(self):
        c = Client()
        logged_in = c.login(username=self.user.username, password='secret')
        self.assertTrue(logged_in)

        response = c.get(reverse('transaction_create'))
        self.assertEqual(200, response.status_code)

    def test_transaction_create_post(self):
        c = Client()
        logged_in = c.login(username=self.user.username, password='secret')
        self.assertTrue(logged_in)

        self.assertEqual(0, Transaction.objects.count())
        response = c.post(reverse('transaction_create'),
                          {'title': 'forty-two',
                           'amount': 42,
                           'category': Transaction.EXPENSE},
                          follow=True)
        self.assertRedirects(response, reverse('transaction_list'))
        self.assertEqual(1, Transaction.objects.count())
        self.assertEqual('forty-two', Transaction.objects.latest('id').title)
        self.assertEqual(42, Transaction.objects.latest('id').amount)
