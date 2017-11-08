"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

#from . import views

from .views import (
    post_main,
    post_chat,
    post_computer,
    post_movie,
    post_game,
    post_drama,
    post_mylog,
    post_detail,
    post_delete,
    post_suggest,
    post_create,
    post_update,
    )

urlpatterns = [
    url(r'^$', post_main, name='pmain'),
    url(r'^chat/$', post_chat, name='pchat'),
    url(r'^computer/$', post_computer, name='pcomputer'),
    url(r'^movie/$', post_movie, name='pmovie'),
    url(r'^game/$', post_game, name='pgame'),
    url(r'^drama/$', post_drama, name='pdrama'),
    url(r'^mylog/$', post_mylog, name='pmylog'),
    url(r'^suggest/$', post_suggest, name='psuggest'),
    url(r'^create/$', post_create, name='create'),
    url(r'^post/(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^post/(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^post/(?P<id>\d+)/delete/$', post_delete, name='delete'),
]

