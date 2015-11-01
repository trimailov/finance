from django.test import TestCase

from books.factories import ReceiptFactory
from books.models import Receipt


class ReceiptTests(TestCase):
    def test_create(self):
        self.assertEqual(0, Receipt.objects.count())
        ReceiptFactory()
        self.assertEqual(1, Receipt.objects.count())
        self.assertEqual('receipt0', Receipt.objects.latest('id').title)
