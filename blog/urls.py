#coding: utf-8
from django.conf.urls import *
from blog.views import PostsListView, PostDetailView

urlpatterns = [
    url(r'^$', PostsListView.as_view(), name='list'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='detail'),
]
