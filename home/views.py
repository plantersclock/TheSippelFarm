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
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


import cx_Oracle
import json
import datetime
import pytz
import pendulum
import uuid

from events.models import Event



class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'




class HomeView(generic.ListView):
    context_object_name = "context"
    template_name = "home/home.html"
    def get_queryset(self):
        print (pendulum.now())
        print (datetime.datetime.now())
        context = {
                'events': Event.objects.filter(published = True, end_date__gte = pendulum.now()).order_by('start_date')
        }

        print (context)

        for event in context['events']:
            print (event)

        return context

    





