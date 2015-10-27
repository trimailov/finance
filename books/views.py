from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from books import models


@login_required
def receipt_list(request, user_id):
    user = User.objects.get(id=user_id)
    ctx = {}
    ctx['user'] = user
    ctx['receipts'] = models.Receipt.objects.filter(user=user).order_by('-id')
    return render(request, 'receipt_list.html', context=ctx)
