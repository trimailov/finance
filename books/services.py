from datetime import datetime
from datetime import timedelta

from django.utils import timezone

from books.models import Transaction


def get_months_transactions():
    today = timezone.now()
    first_day_of_a_month = datetime(today.year, today.month, 1,
                                    tzinfo=today.tzinfo)
    qs = Transaction.objects.filter(created__gte=first_day_of_a_month)
    return qs


def get_last_months_transactions():
    first_day_of_a_month = timezone.now().replace(day=1)
    last_month = first_day_of_a_month - timedelta(days=1)
    first_day_of_last_month = datetime(last_month.year, last_month.month, 1,
                                       tzinfo=last_month.tzinfo)
    qs = Transaction.objects.filter(created__gte=first_day_of_last_month)
    return qs


def get_this_years_transactions():
    today = timezone.now()
    first_day_of_this_year = datetime(today.year, 1, 1, tzinfo=today.tzinfo)
    qs = Transaction.objects.filter(created__gte=first_day_of_this_year)
    return qs
