from django.conf.urls import url

from books import views


urlpatterns = [
    url(r'^(?P<user_id>[0-9]+)/$',
        views.receipt_list,
        name='receipt_list'),
    url(r'^(?P<user_id>[0-9]+)/create/$',
        views.receipt_create,
        name='receipt_create'),
]
