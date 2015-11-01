from django.conf.urls import include, url

from accounts import views


urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^login_redirect/$', views.login_redirect, name='login_redirect'),
]
