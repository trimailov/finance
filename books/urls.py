from django.conf.urls import url

from books import views


urlpatterns = [
    url(r'^$', views.transaction_list, name='transaction_list'),
    url(r'^create/$', views.transaction_create, name='transaction_create'),
    url(r'^update/(?P<id>\d+)/$', views.transaction_update,
        name='transaction_update'),
]
