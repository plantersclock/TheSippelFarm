import datetime
import pytz
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
from bootstrap_datepicker_plus import DateTimePickerInput
from django.contrib.auth.models import User

# Create your models here.

class MixPanel(models.Model):
    date = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return "Mixpanel date={}".format(self.date)

class Professional(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=1000, null=True, default=None, blank=True)

    def __str__(self):
        return "{}".format(self.name)

class Event(models.Model):
    name = models.CharField(max_length=128)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    start_date = models.DateTimeField('Event Start Date')
    end_date = models.DateTimeField('Event End Date')
    details =  models.TextField('Event Details')
    photo = models.CharField(max_length=1000, null=True, default=None, blank=True)
    published = models.BooleanField()

    def __str__(self):
        return "{}: {}-{}".format(self.name, self.start_date, self.end_date)

class EventUser(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    email= models.EmailField(max_length=256)
    rider = models.CharField("Rider's Name", max_length=128)
    horse = models.CharField("Horse's Name", max_length=128)
    notes = models.TextField('Scheduling Notes', null=True, default=None, blank=True)

    def __str__(self):
        return "{}: {}-{}".format(self.event.name, self.rider, self.horse)
