from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from datetime import date, datetime, timezone, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from pytz import timezone
import requests
import csv


import cx_Oracle
import json
import datetime
import pytz
import pendulum
import uuid


from .models import (
    Event,
    EventJoined,
    ScheduledAttendee
)
from .forms import (
    EventSignUpForm,
    AttendeeScheduleForm
)

from django.core.mail import send_mail



class AboutView(generic.ListView):
    template_name = "events/about_me.html"
    context_object_name = "mixpanel"

    def get_queryset(self):

        return "hi"


class EventsView(generic.ListView):
    model = Event
    template_name = "events/events.html"
    context_object_name = "events"

    def get_queryset(self):
        context = {
            "events": Event.objects.filter(published = True).order_by('start_date'),
        }
        print(context)
        return context


def event_sign_up(request, pk):
    event = get_object_or_404(Event, pk=pk)
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = EventSignUpForm(
            request.POST
        )
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            new_sign_up = form.save(commit=False)
            new_sign_up.event = event
            try:
                new_sign_up.save()
                return HttpResponseRedirect("/events")
            except:
                context = {
                    "error": "This rider and horse are already signed up for this event",
                    "event": event,
                    "form": form,
                }
                return render(request, "events/sign_up.html", context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventSignUpForm()

    context = {
        "event": event,
        "form": form,
    }
    return render(request, "events/sign_up.html", context)

def attendee_schedule(request, pk):

    if request.method == "POST":
        form = AttendeeScheduleForm(request.POST)

        if ScheduledAttendee.objects.filter(attendee = form['attendee'].value()).exists():
            scheduled_attendee = ScheduledAttendee.objects.get(attendee=form.data.get('attendee'))
            form = AttendeeScheduleForm(request.POST or None, instance=scheduled_attendee)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/events/{}/scheduler".format(pk))

        else:
            if form.is_valid():
                new_scheduled = form.save(commit=False)
                attendee = get_object_or_404(EventJoined, pk=form['attendee'].value())
                new_scheduled.attendee = attendee
                new_scheduled.save()
                print("New Thing")
                return HttpResponseRedirect("/events/{}/scheduler".format(pk))

    else:
        form = AttendeeScheduleForm()
        form.fields['attendee'].queryset = EventJoined.objects.filter(event=pk)
        form.fields['attendee'].empty_label = None

    context = {
        "form": form,
    }
    return render(request, "events/scheduler.html", context)
