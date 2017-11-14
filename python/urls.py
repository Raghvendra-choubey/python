from django.conf.urls import url

import database_connection.views

urlpatterns = [
    url(r'^$', database_connection.views.index, name='index'),
    url(r'^login', database_connection.views.login, name='login'),
]
