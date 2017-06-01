#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from .views import index, blog_add,comment_add

urlpatterns = [
    url(r'comment/blog_add/(?P<blog>[0-9]*)/', blog_add, name="blog_add"),
    url(r'comment/comment_add/(?P<comment>[0-9]*)/', comment_add, name="comment_add"),
    url(r'', index, name="index"),

]
