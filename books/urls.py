from django.conf.urls import url

from books import views


urlpatterns = [
    url(r'^transactions/$', views.transaction_list, name='transaction_list'),
    url(r'^create/$', views.transaction_create, name='transaction_create'),
    url(r'^delete/(?P<pk>\d+)/$', views.transaction_delete,
        name='transaction_delete'),
    url(r'^update/(?P<pk>\d+)/$', views.transaction_update,
        name='transaction_update'),
    url(r'^filter/$', views.transaction_list_filter,
        name='transaction_list_filter'),

    url(r'^debts-loans/$', views.debt_loan_list, name='debt_loan_list'),
    url(r'^debts-loans/create/$', views.debt_loan_create,
        name='debt_loan_create'),
    url(r'^debts-loans/delete/(?P<pk>\d+)/$', views.debt_loan_delete,
        name='debt_loan_delete'),
    url(r'^debts-loans/update/(?P<pk>\d+)/$', views.debt_loan_update,
        name='debt_loan_update'),
]
