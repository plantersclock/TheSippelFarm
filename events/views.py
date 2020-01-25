from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse
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
    AttendeeScheduleForm,
    EventForm
)

from django.core.mail import send_mail
from django.conf import settings



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
            "events": Event.objects.filter(published = True, end_date__gte = pendulum.now()).order_by('start_date'),
        }
        print(context)
        return context

class LiveView(generic.ListView):
    model = Event
    template_name = "events/live.html"
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
                print(new_sign_up.email)
                new_sign_up.save()
                print (new_sign_up.event.name)
                subject = '{}'.format(new_sign_up.event.name)
                message = 'We are excited to see you there!'
                email_from = settings.EMAIL_HOST_USER
                print(settings.EMAIL_HOST_USER)
                recipient_list = [new_sign_up.email,]
                print ("hi")
                send_mail( subject, message, email_from, recipient_list )
                return HttpResponseRedirect("/events")
            except:
                context = {
                    "error": "This Rider and Horse are already signed up for this event",
                    "event": event,
                    "form": form
                }
                return render(request, "events/sign_up.html", context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventSignUpForm()

    scheduled_attendees = ScheduledAttendee.objects.filter(attendee__event = pk).order_by('time').order_by('day')

    try:
        if event.signup_end_date > date.today() > event.signup_start_date:
            print ("Disp signup")
            disp_signup = True
        else:
            disp_signup = False
    except:
        disp_signup = False
    context = {
        "event": event,
        "form": form,
        "disp_signup": disp_signup,
        "scheduled_attendees": list(scheduled_attendees)
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


    context = {
        "form": form,
        "scheduled_attendees": ScheduledAttendee.objects.filter(attendee__event=pk).exclude(day=None).order_by('time'),
        "event": get_object_or_404(Event, id=pk)
    }
    return render(request, "events/scheduler.html", context)

def attendee_defaults(request):
    attendee = request.GET.get('attendee', None)
    if ScheduledAttendee.objects.filter(attendee=attendee).exists():
        data = {
            'is_scheduled': ScheduledAttendee.objects.filter(attendee=attendee).exists(),
            'date': ScheduledAttendee.objects.get(attendee=attendee).day,
            'time': ScheduledAttendee.objects.get(attendee=attendee).time,
            'duration': ScheduledAttendee.objects.get(attendee=attendee).duration,
            'notes': EventJoined.objects.get(id=attendee).notes
        }
    else:
        data = {
            'is_scheduled': False,
            'notes': EventJoined.objects.get(id=attendee).notes
        }


    return JsonResponse(data)


class EventAdminView(generic.ListView):
    model = Event
    template_name = "events/event_admin.html"
    context_object_name = "context"

    def get_queryset(self):
        events = Event.objects.filter(end_date__gte = pendulum.now()-timedelta(days=60)).order_by('start_date')
        event_list = []
        for event in events:
            event_with_counts = {"event": event,
                                "joined": EventJoined.objects.filter(event=event).count(),
                                "scheduled": ScheduledAttendee.objects.filter(attendee__event=event).count()
            }
            event_list.append(event_with_counts)
        context = {
            "events": event_list,
        }
        return context

def add_event(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            form.save()
            return HttpResponseRedirect("/events/admin")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = EventForm()

    context = {
        "title": "Add Event",
        "form": form,
    }
    return render(request, "events/event_form.html", context)



def edit_event(request, pk):
    instance = get_object_or_404(Event, id=pk)
    form = EventForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if '_schedule' in request.POST:
            return HttpResponseRedirect("/events/{}/scheduler".format(pk))
        if '_submit' in request.POST:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/events/admin")
    context = {
        "pk": pk,
        "title": "Edit Event",
        "form": form,
    }
    return render(request, "events/event_form.html", context)

