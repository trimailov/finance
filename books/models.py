from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields


class Receipt(models.Model):
    title = fields.CharField(max_length=255)
    price = fields.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User)

    def __str__(self):
        return "{}_{}".format(self.title, self.price)
