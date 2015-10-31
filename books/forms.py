from django import forms

from books import models


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = models.Receipt
        fields = ['title', 'price']
