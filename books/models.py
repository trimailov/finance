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
    active = fields.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.title)

    def deactivate(self):
        if self.active:
            self.active = False
            self.save()


class DebtLoan(models.Model):
    DEBT = 0
    LOAN = 1
    CATEGORY_CHOICES = (
        (DEBT, 'debt'),
        (LOAN, 'loan'),
    )

    with_who = fields.CharField(max_length=255)
    title = fields.CharField(max_length=255, null=True, blank=True)
    amount = fields.DecimalField(max_digits=10, decimal_places=2)
    category = fields.PositiveSmallIntegerField(choices=CATEGORY_CHOICES)
    created = fields.DateTimeField(default=timezone.now, editable=False)
    modified = fields.DateTimeField(default=timezone.now)
    active = fields.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.title:
            return "{}: {}".format(self.with_who, self.title)
        else:
            return "{}".format(self.with_who)

    def deactivate(self):
        if self.active:
            self.active = False
            self.save()
