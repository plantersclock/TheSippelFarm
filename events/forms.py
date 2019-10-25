from django import forms

from django.contrib.admin import widgets

from bootstrap_datepicker_plus import DateTimePickerInput, DatePickerInput, TimePickerInput
from django.contrib.admin import widgets

import datetime
from .models import (
    EventJoined,
    ScheduledAttendee
)

class EventSignUpForm(forms.ModelForm):
    class Meta:
        model = EventJoined
        fields = ["email", "rider", "horse", "notes"]

class AttendeeScheduleForm(forms.ModelForm):
    # pk = forms.ModelChoiceField(
    #     queryset=EventJoined.objects.all(),
    #     empty_label=None,
    # )

    class Meta:
        model = ScheduledAttendee
        fields = ["attendee", "day", "time", "duration"]
        widgets = { "day": DatePickerInput(attrs={"onfocus":"blur()"}) ,
                    "time": TimePickerInput(attrs={"InputType":"TYPE_NULL"})
                }
