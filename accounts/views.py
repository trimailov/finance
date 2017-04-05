from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import reverse
from django.shortcuts import redirect


def login(request, *args, **kwargs):
    if request.method == 'POST':
        # set login session cookie for 1 year
        request.session.set_expiry(3600 * 24 * 365)
    return auth_views.login(request, *args, **kwargs)


@login_required
def login_redirect(request):
    return redirect(reverse('transaction_list'))
