from django import forms

from books import models


class TransactionForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = ['title', 'amount', 'category']


class DebtLoanForm(forms.ModelForm):
    class Meta:
        model = models.DebtLoan
        fields = ['with_who', 'title', 'amount', 'category']
