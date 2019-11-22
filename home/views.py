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
from .models import Page, PageContent, ForSaleItems
from .forms import ContactUsForm

from django.core.mail import send_mail
from django.conf import settings



class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



class HomeView(generic.ListView):
    context_object_name = "context"
    template_name = "home/home.html"
    def get_queryset(self):
        context = {
            'events': Event.objects.filter(published = True, end_date__gte = pendulum.now()).order_by('start_date')
        }
        return context


def page(request, name):
    page = get_object_or_404(Page, published = True, page_title = name)
    print(page)
    context = {
        'page': page,
        'page_content': PageContent.objects.filter(published = True, page = page).order_by('order')
    }

    return render(request, "home/page.html", context)

def for_sale(request):
    context = {
        'for_sale_items': ForSaleItems.objects.filter(published = True).order_by('order')
    }

    return render(request, "home/for-sale.html", context)

def contact_us(request, ref):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ContactUsForm(
            request.POST
        )
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            contact_us = form.cleaned_data
            try:
                subject = '{} Message From {}: {}'.format(ref, contact_us['name'], contact_us['email'])
                message = contact_us['message']
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['mattman861@gmail.com',]
                send_mail( subject, message, email_from, recipient_list )
                if ref == "contact-us":
                    return HttpResponseRedirect("/")
                else:
                    return HttpResponseRedirect("/for-sale")
            except:
                context = {
                    "error": "Something went wrong :(",
                    "form": form,
                }
                return render(request, "home/contact-us.html", context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactUsForm()

    context = {
        "form": form,
    }
    return render(request, "home/contact-us.html", context)




