#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2017 Jeremy Low

"""dsa_signin_sheets URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from signin_sheets.views import (
    event_participants,
    event_signin,
    event_to_csv,
    user_logout,
    FirstRun,
    EventCreateView,
    EventDetailView,
    EventListView,
    EventDeleteView,
    HomePageView,
)

urlpatterns = [
    url(r"^$", HomePageView.as_view(), name="home"),
    url(r"^login/$", auth_views.LoginView.as_view(), name="login"),
    url(r"^logout/$", user_logout, name="logout"),
    url(r"^admin/", admin.site.urls),
    url(r"^start/$", FirstRun.as_view(), name="start"),
    url(r"^event/list/$", EventListView.as_view(), name="event-list"),
    url(r"^event/new/$", EventCreateView.as_view(), name="event-create"),
    url(
        r"^event/(?P<pk>[0-9]+)/delete/$",
        EventDeleteView.as_view(),
        name="event-delete",
    ),
    url(r"^event/(?P<pk>[0-9]+)/signin/$", event_signin, name="event-signin"),
    url(
        r"^event/(?P<pk>[0-9]+)/participants/$",
        event_participants,
        name="event-participants",
    ),
    url(r"^event/(?P<pk>[0-9]+)/export/$", event_to_csv, name="event-export"),
    url(r"^event/(?P<pk>[0-9]+)/$", EventDetailView.as_view(), name="event-detail"),
]
