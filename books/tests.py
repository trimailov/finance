from django.core.urlresolvers import reverse
from django.test import Client
from django.test import TestCase

from books.factories import ReceiptFactory
from books.factories import UserFactory
from books.models import Receipt


class ReceiptTests(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_create_model(self):
        self.assertEqual(0, Receipt.objects.count())
        ReceiptFactory()
        self.assertEqual(1, Receipt.objects.count())
        self.assertEqual(str(Receipt.objects.latest('id')), 'receipt0_10.00')

    def test_receipt_create_get(self):
        c = Client()
        logged_in = c.login(username=self.user.username, password='secret')
        self.assertTrue(logged_in)

        response = c.get(reverse('receipt_create'))
        self.assertEqual(200, response.status_code)

    def test_receipt_create_post(self):
        c = Client()
        logged_in = c.login(username=self.user.username, password='secret')
        self.assertTrue(logged_in)

        self.assertEqual(0, Receipt.objects.count())
        response = c.post(reverse('receipt_create'),
                          {'title': 'forty-two', 'price': 42},
                          follow=True)
        self.assertRedirects(response, reverse('receipt_list'))
        self.assertEqual(1, Receipt.objects.count())
        self.assertEqual('forty-two', Receipt.objects.latest('id').title)
        self.assertEqual(42, Receipt.objects.latest('id').price)
