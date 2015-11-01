import factory

from accounts.factories import UserFactory
from books import models


class ReceiptFactory(factory.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'receipt%d' % n)
    price = 10
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = models.Receipt
