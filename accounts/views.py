from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


@login_required
def login_redirect(request):
    return redirect(reverse('receipt_list'))
