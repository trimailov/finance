from django.conf.urls import include, url

from accounts import views


urlpatterns = [
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_redirect/$', views.login_redirect, name='login_redirect'),
]
