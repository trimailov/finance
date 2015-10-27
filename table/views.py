from django.shortcuts import render


def table(request):
    return render(request, 'table.html')
