#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2017 Jeremy Low

from django.conf import settings
from django.contrib.auth import get_user, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, reverse

from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, FormView, DeleteView

from signin_sheets.models import Event


class FirstRun(CreateView):
    """Initialize app & create first user."""

    model = settings.AUTH_USER_MODEL
    template_name = 'first_run.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class EventCreateView(LoginRequiredMixin, CreateView):
    """Create a new event."""

    model = Event
    fields = ['name', 'event_date']

    def form_valid(self, form):
        resp = super().form_valid(form)
        self.object.event_admin = get_user(self.request)
        self.object.save()
        return resp


class EventDetailView(LoginRequiredMixin, DetailView):
    """Show details for a given event."""

    model = Event


class EventListView(LoginRequiredMixin, ListView):
    """List all events for the current user."""

    model = Event

    def get_queryset(self):
        return Event.objects.all().filter(event_admin=self.request.user.id)


class EventDeleteView(LoginRequiredMixin, DeleteView):
    """Delete an event from the system."""

    model = Event
    success_url = reverse_lazy('event-list')


def event_signin(request, *args, **kwargs):
    if not request.user.is_anonymous():
        logout(request)

    if request.method == "GET":
        pass
    return redirect(reverse('event-list'))
