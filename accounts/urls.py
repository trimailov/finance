from django.conf.urls import include, url
from django.contrib.auth.views import logout as auth_logout
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete

from accounts import views


urlpatterns = [
    url(r'^logout/$', auth_logout, name='logout'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_redirect/$', views.login_redirect, name='login_redirect'),
    url(r'^reset/$', password_reset, name='password_reset'),
    url(r'^reset-done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^reset-complete/$', password_reset_complete, name='password_reset_complete'),
    url(r'^', include('registration.backends.simple.urls')),
]
