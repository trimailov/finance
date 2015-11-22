import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

import factory

from accounts.factories import UserFactory
from books.factories import TransactionFactory
from books.models import Transaction


class Command(BaseCommand):
    help = "Popoulates databse with dummy data"

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin'):
            self.create_admin()
        else:
            self.admin = User.objects.get(username='admin')
            print("admin user already exists")

        self.create_transactions()

    def create_admin(self):
        # Factory creates simple user, so ``is_staff`` is set later
        self.admin = UserFactory(username='admin', password='asdasd')
        self.admin.is_staff = True
        self.admin.is_superuser = True
        self.admin.save()
        print("admin user have been created successfully")

    def create_transactions(self):
        TransactionFactory.create_batch(
            10,
            amount=factory.Sequence(lambda n: random.randrange(0, 10)),
            category=random.choice([Transaction.EXPENSE, Transaction.INCOME]),
            user=self.admin,
        )
        print("Transactions for admin created")
