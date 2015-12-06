from datetime import date
from datetime import timedelta

from django.utils import timezone

from books.models import Transaction


def get_months_transactions():
    today = timezone.now()
    first_day_of_a_month = date(today.year, today.month, 1)
    qs = Transaction.objects.filter(created__gte=first_day_of_a_month)
    return qs


def get_last_months_transactions():
    first_day_of_a_month = timezone.now().replace(day=1)
    last_month = first_day_of_a_month - timedelta(days=1)
    first_day_of_last_month = date(last_month.year, last_month.month, 1)
    qs = Transaction.objects.filter(created__gte=first_day_of_last_month)
    return qs


def get_this_years_transactions():
    today = timezone.now()
    first_day_of_this_year = date(today.year, 1, 1)
    qs = Transaction.objects.filter(created__gte=first_day_of_this_year)
    return qs
