#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from message import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^sent/(?P<touser>[0-9]+)/$', views.message_sent),
    url(r'^message/(?P<fromuser>[0-9]*)/(?P<touser>[0-9]*)', views.message_add,
        name="message_add"),
    url(r'^(?P<fromuser>[0-9]+)/', views.read_messages, name='read_message'),
    url(r'^', views.index, name='index'),
]
