from django.contrib import admin

from books.models import DebtLoan
from books.models import Transaction

admin.site.register(Transaction)
admin.site.register(DebtLoan)
