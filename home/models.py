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

