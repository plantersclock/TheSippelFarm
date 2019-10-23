from django import forms

from django.contrib.admin import widgets

from bootstrap_datepicker_plus import DateTimePickerInput, DatePickerInput, TimePickerInput
from django.contrib.admin import widgets

import datetime
from .models import (
    EventJoined,
)

class EventSignUpForm(forms.ModelForm):
    class Meta:
        model = EventJoined
        fields = ["email", "rider", "horse", "notes"]

class AttendeeScheduleForm(forms.ModelForm):
    class Meta:
        model = EventJoined
        fields = ["day", "time", "duration"]
        widgets = {"day": DatePickerInput(),
                    "time": TimePickerInput()
                }
