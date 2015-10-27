from django.conf.urls import url

from table import views


urlpatterns = [
    url(r'^', views.table),
]
