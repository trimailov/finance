from django.conf.urls import url

from books import views


urlpatterns = [
    url(r'^(?P<user_id>[0-9]+)/$', views.receipt_list),
]
