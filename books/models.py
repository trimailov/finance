from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.utils import timezone


class Transaction(models.Model):
    title = fields.CharField(max_length=255)
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    created = fields.DateTimeField(auto_now=True)
    modified = fields.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User)

    def __str__(self):
        return "{}_{}".format(self.title, self.price)
