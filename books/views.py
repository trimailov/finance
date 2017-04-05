from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from books.models import DebtLoan
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
        user_transactions = Transaction.objects.filter(user=user, active=True)
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

    ctx['list'] = 'transactions'

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
def transaction_delete(request, pk):
    Transaction.objects.get(pk=pk).deactivate()
    return redirect(reverse('transaction_list'))


@login_required
def transaction_update(request, pk):
    instance = get_object_or_404(Transaction, pk=pk)
    form = forms.TransactionForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect(reverse('transaction_list'))
    return render(request, 'transaction_create.html', {'form': form})


@login_required
def debt_loan_list(request):
    ctx = {}

    user_id = request.user.id
    user = User.objects.get(id=user_id)

    user_debt_loans = DebtLoan.objects.filter(user=user, active=True)

    user_debt_loans = user_debt_loans.order_by('-created')

    ctx['user'] = user
    ctx['debt_loans'] = user_debt_loans
    ctx['debt_sum'] = user_debt_loans \
        .filter(category=DebtLoan.DEBT) \
        .aggregate(Sum('amount')).get('amount__sum')
    ctx['loan_sum'] = user_debt_loans \
        .filter(category=DebtLoan.LOAN) \
        .aggregate(Sum('amount')).get('amount__sum')

    ctx['list'] = 'debts_loans'

    return render(request, 'debt_loan_list.html', context=ctx)


@login_required
def debt_loan_create(request):
    form = forms.DebtLoanForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect(reverse('debt_loan_list'))
    return render(request, 'debt_loan_create.html', {'form': form})


@login_required
def debt_loan_delete(request, pk):
    DebtLoan.objects.get(pk=pk).deactivate()
    return redirect(reverse('debt_loan_list'))


@login_required
def debt_loan_update(request, pk):
    instance = get_object_or_404(DebtLoan, pk=pk)
    form = forms.DebtLoanForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect(reverse('debt_loan_list'))
    return render(request, 'debt_loan_create.html', {'form': form})
