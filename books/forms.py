from django import forms

from books import models


class TransactionForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = ['title', 'amount', 'category']
