import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import IntegrityError

import factory

from accounts.factories import UserFactory
from books.factories import TransactionFactory


class Command(BaseCommand):
    help = "Popoulates databse with dummy data"

    def handle(self, *args, **options):
        # Factory creates simple user, so ``is_staff`` is set later
        try:
            admin = UserFactory(username='admin', password='asdasd')
            admin.is_staff = True
            admin.save()
            print("admin user have been created successfully")
        except IntegrityError:
            admin = User.objects.get(username='admin')
            print("admin user already exists")

        TransactionFactory.create_batch(
            10,
            price=factory.Sequence(lambda n: random.randrange(0, 10)),
            user=admin,
        )
        print("Transactions for admin created")
