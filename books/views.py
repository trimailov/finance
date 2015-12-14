from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from books.models import Transaction
from books import forms
from books import services


@login_required
def transaction_list(request):
    ctx = {}

    user_id = request.user.id
    user = User.objects.get(id=user_id)

    fltr = request.session.get('filter:transaction_list', None)
    if fltr == "last_month":
        user_transactions = services.get_last_months_transactions(user)
        ctx['fltr'] = fltr
    elif fltr == "this_year":
        user_transactions = services.get_this_years_transactions(user)
        ctx['fltr'] = fltr
    elif fltr == "all_time":
        user_transactions = Transaction.objects.filter(user=user)
        ctx['fltr'] = fltr
    else:
        # make 'this_month' filter default
        user_transactions = services.get_months_transactions(user)
        ctx['fltr'] = 'this_month'

    user_transactions = user_transactions.order_by('-created')

    ctx['user'] = user
    ctx['transactions'] = user_transactions
    ctx['negative_transaction_sum'] = user_transactions \
        .filter(category=Transaction.EXPENSE) \
        .aggregate(Sum('amount')).get('amount__sum')
    ctx['positive_transaction_sum'] = user_transactions \
        .filter(category=Transaction.INCOME) \
        .aggregate(Sum('amount')).get('amount__sum')

    return render(request, 'transaction_list.html', context=ctx)


@login_required
def transaction_list_filter(request):
    fltr = request.GET.get('filter', None)
    request.session['filter:transaction_list'] = fltr
    return redirect(reverse('transaction_list'))


@login_required
def transaction_create(request):
    form = forms.TransactionForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect(reverse('transaction_list'))
    return render(request, 'transaction_create.html', {'form': form})


@login_required
def transaction_update(request, id):
    instance = get_object_or_404(Transaction, id=id)
    form = forms.TransactionForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect(reverse('transaction_list'))
    return render(request, 'transaction_create.html', {'form': form})
