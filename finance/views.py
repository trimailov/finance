from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render


def home(request):
    if request.user.is_authenticated():
        return redirect(reverse('receipt_list'))
    return render(request, 'index.html')
