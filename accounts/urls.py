from django.conf.urls import include, url
from django.contrib.auth.views import logout as auth_logout
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete

from accounts import views


urlpatterns = [
    # login/logout
    url(r'^logout/$', auth_logout, name='logout'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_redirect/$', views.login_redirect, name='login_redirect'),

    url(r'^settings/(?P<pk>\d+)/$', views.user_settings,
        name='user_settings'),

    # password reset
    url(r'^password-reset/$',
        password_reset,
        {'template_name': 'password_reset.html'},
        name='password_reset'),
    url(r'^password-reset-done/$',
        password_reset_done,
        {'template_name': 'password_reset_done.html'},
        name='password_reset_done'),
    url(r'^password-reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm,
        {'template_name': 'password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^password-reset-complete/$',
        password_reset_complete,
        {'template_name': 'password_reset_complete.html'},
        name='password_reset_complete'),

    url(r'^', include('registration.backends.simple.urls')),
]
