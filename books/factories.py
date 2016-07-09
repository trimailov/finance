import factory

from accounts.factories import UserFactory
from books import models


class TransactionFactory(factory.DjangoModelFactory):
    title = factory.Sequence(lambda n: 'transaction_%d' % n)
    amount = 10
    category = models.Transaction.EXPENSE
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = models.Transaction


class DebtLoanFactory(factory.DjangoModelFactory):
    with_who = "ACME co."
    title = factory.Sequence(lambda n: 'debt_loan_%d' % n)
    amount = 42
    category = models.DebtLoan.DEBT
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = models.DebtLoan
