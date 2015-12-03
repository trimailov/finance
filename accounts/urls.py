from django.conf.urls import include, url
from django.contrib.auth.views import logout as auth_logout

from accounts import views


urlpatterns = [
    url(r'^logout/$', auth_logout, name='logout'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_redirect/$', views.login_redirect, name='login_redirect'),
    url(r'^', include('registration.backends.simple.urls')),
]
