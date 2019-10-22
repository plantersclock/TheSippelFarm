from django import forms

from django.contrib.admin import widgets

from bootstrap_datepicker_plus import DateTimePickerInput, DatePickerInput
from django.contrib.admin import widgets

import datetime
from .models import (
    EventUser
)

class EventSignUpForm(forms.ModelForm):
    class Meta:
        model = EventUser
        fields = ["email", "rider", "horse", "notes"]

