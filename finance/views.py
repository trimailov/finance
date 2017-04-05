from django.urls import reverse
from django.shortcuts import redirect


def home(request):
    if request.user.is_authenticated():
        return redirect(reverse('transaction_list'))
    return redirect(reverse('login'))
