from datetime import datetime
from datetime import timedelta

import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone

import factory
import pytz

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

    def _get_last_month(self):
        "Returns random date in last month"
        today = timezone.now()
        first_month_day = today.replace(day=1)
        last_month = first_month_day - timedelta(days=1)
        return datetime(last_month.year,
                        last_month.month,
                        random.randint(1, 28),
                        tzinfo=pytz.utc)

    def _get_this_year(self):
        "Returns random date in this year"
        today = timezone.now()
        return datetime(today.year,
                        random.randint(1, today.month),
                        random.randint(1, today.day),
                        tzinfo=pytz.utc)

    def _get_all_time(self):
        "Returns random date"
        today = timezone.now()
        return datetime(random.randint(2000, today.year-1),
                        random.randint(1, 12),
                        random.randint(1, 28),
                        tzinfo=pytz.utc)

    def create_transactions(self):
        categories = [Transaction.EXPENSE, Transaction.INCOME]

        # create now
        TransactionFactory.create_batch(
            5,
            amount=factory.Sequence(lambda n: random.randint(1, 10)),
            category=factory.Sequence(lambda n: random.choice(categories)),
            user=self.admin,
        )

        # create for last month
        TransactionFactory.create_batch(
            5,
            amount=factory.Sequence(lambda n: random.randint(1, 10)),
            category=factory.Sequence(lambda n: random.choice(categories)),
            user=self.admin,
            created=factory.Sequence(lambda n: self._get_last_month()),
        )

        # create for this year
        TransactionFactory.create_batch(
            5,
            amount=factory.Sequence(lambda n: random.randint(1, 10)),
            category=factory.Sequence(lambda n: random.choice(categories)),
            user=self.admin,
            created=factory.Sequence(lambda n: self._get_this_year()),
        )

        # create for all time
        TransactionFactory.create_batch(
            5,
            amount=factory.Sequence(lambda n: random.randint(1, 10)),
            category=factory.Sequence(lambda n: random.choice(categories)),
            user=self.admin,
            created=factory.Sequence(lambda n: self._get_all_time()),
        )
        print("Transactions for admin created")
