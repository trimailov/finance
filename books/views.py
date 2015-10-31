from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from books import models
from books import forms


@login_required
def receipt_list(request, user_id):
    user = User.objects.get(id=user_id)
    ctx = {}
    ctx['user'] = user
    ctx['receipts'] = models.Receipt.objects.filter(user=user).order_by('-id')
    return render(request, 'receipt_list.html', context=ctx)


@login_required
def receipt_create(request, user_id):
    if request.method == "POST":
        form = forms.ReceiptForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            models.Receipt.objects.create(title=data.get("title"),
                                          price=data.get("price"),
                                          user=request.user)
            return HttpResponseRedirect(reverse('receipt_list',
                                                args=[request.user.id]))
    else:
        form = forms.ReceiptForm()

    return render(request, 'receipt_create.html', {'form': form})
