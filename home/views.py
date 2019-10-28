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



class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'




class HomeView(generic.ListView):

    template_name = "home/home.html"
    def get_queryset(self):

        return "hi"





