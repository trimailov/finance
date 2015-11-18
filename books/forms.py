from django import forms

from books import models


class TransactionForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = ['title', 'amount', 'category']

    def full_clean(self, *args, **kwargs):
        super().full_clean(*args, **kwargs)
