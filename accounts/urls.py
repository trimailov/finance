from django.conf.urls import include, url

from accounts import views
from registration.backends.simple.views import RegistrationView


urlpatterns = [
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_redirect/$', views.login_redirect, name='login_redirect'),
    url(r'^register/$', RegistrationView.as_view(), name='register'),
]
