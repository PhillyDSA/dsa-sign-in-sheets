#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2017 Jeremy Low
import csv

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, reverse

from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, FormView, DeleteView

from signin_sheets.models import Event, EventParticipant
from signin_sheets.forms import ParticipantSigninForm


class HomePageView(TemplateView):
    """Front page kind of view."""

    template_name = 'signin_sheets/home.html'


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

    event = Event.objects.get(pk=kwargs.get('pk', None))

    if request.method == "GET":
        return render(request,
                      'signin_sheets/participant_signin.html',
                      {'form': ParticipantSigninForm,
                       'event': event})
    elif request.method == "POST":
        form = ParticipantSigninForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.event = Event.objects.get(pk=kwargs.get('pk'))
            user.save()
            messages.success(request, "Your information has been saved.<br>Thanks for signing in!")

            return redirect(reverse('event-signin',
                                    kwargs={'pk': kwargs.get('pk')}))
    return redirect(reverse('event-list'))


@login_required
def event_participants(request, *args, **kwargs):
    event = Event.objects.get(pk=kwargs.get('pk', None))
    if event.event_admin.id != request.user.id:
        return HttpResponseForbidden()
    participants = EventParticipant.objects.all().filter(event=event)
    return render(request,
                  'signin_sheets/participant_list.html',
                  {'participants': participants,
                   'event': event})


@login_required
def event_to_csv(request, *args, **kwargs):
    event = Event.objects.get(pk=kwargs.get('pk', None))
    if event.event_admin.id != request.user.id:
        return HttpResponseForbidden()
    participants = EventParticipant.objects.all().filter(event=event)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{ event.id }.csv"'

    writer = csv.writer(response)
    writer.writerow([
            'first_name',
            'last_name',
            'email',
            'street_one',
            'street_two',
            'state',
            'zip_code',
            'telephone_number',
        ])
    for part in participants:
        writer.writerow([
            part.first_name,
            part.last_name,
            part.email,
            part.street_one,
            part.street_two,
            part.state,
            part.zip_code,
            part.telephone_number,])
    return response


def user_logout(request):
    logout(request)
    return redirect('/')
