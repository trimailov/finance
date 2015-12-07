from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.utils import timezone


class Transaction(models.Model):
    EXPENSE = 'exp'
    INCOME = 'inc'
    CATEGORY_CHOICES = (
        (EXPENSE, 'expense'),
        (INCOME, 'income'),
    )

    title = fields.CharField(max_length=255)
    amount = fields.DecimalField(max_digits=10, decimal_places=2)
    category = fields.CharField(max_length=3, choices=CATEGORY_CHOICES)
    created = fields.DateTimeField(default=timezone.now, editable=False)
    modified = fields.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User)

    def __str__(self):
        return "{}".format(self.title)
