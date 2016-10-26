from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from accounts import forms


def login(request, *args, **kwargs):
    if request.method == 'POST':
        # set login session cookie for 1 year
        request.session.set_expiry(3600*24*365)
    return auth_views.login(request, *args, **kwargs)


@login_required
def login_redirect(request):
    return redirect(reverse('transaction_list'))


@login_required
def user_settings(request, pk):
    instance = get_object_or_404(User, pk=pk)
    form = forms.UserSettingsForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect(reverse('transaction_list'))
    return render(request, 'user_settings.html', {'form': form})
