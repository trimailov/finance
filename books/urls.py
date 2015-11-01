from django.conf.urls import url

from books import views


urlpatterns = [
    url(r'^$', views.receipt_list, name='receipt_list'),
    url(r'^create/$', views.receipt_create, name='receipt_create'),
]
