from django import forms

from django.contrib.admin import widgets

from bootstrap_datepicker_plus import DateTimePickerInput, DatePickerInput, TimePickerInput
from django.contrib.admin import widgets

import datetime
from .models import (
    EventJoined,
    ScheduledAttendee,
    Event
)

class EventSignUpForm(forms.ModelForm):
    class Meta:
        model = EventJoined
        fields = ["email", "rider", "horse", "payment", "notes"]
        widgets = { "payment": forms.Select(attrs={"class":"form-control"}),}

class AttendeeScheduleForm(forms.ModelForm):
    # pk = forms.ModelChoiceField(
    #     queryset=EventJoined.objects.all(),
    #     empty_label=None,
    # )

    class Meta:
        model = ScheduledAttendee
        fields = ["attendee", "day", "time", "duration"]
        widgets = { "attendee": forms.Select(attrs={"class":"form-control"}),
                    "day": DatePickerInput(options= {"ignoreReadonly":True}, attrs={"readonly":"readonly", "style":"background-color:white; border: 1px solid #ced4da;"}),
                    "time": TimePickerInput(options= {"ignoreReadonly":True}, attrs={"readonly":"readonly", "style":"background-color:white; border: 1px solid #ced4da;"}),
                    "duration": forms.NumberInput(attrs={"class":"form-control"})
                }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "professional", "start_date", "end_date", "details", "published"]
        widgets = {
            "start_date": DateTimePickerInput(options= {"ignoreReadonly":True}, attrs={"readonly":"readonly", "style":"background-color:white; border: 1px solid #ced4da;"}),
            "end_date": DateTimePickerInput(options= {"ignoreReadonly":True}, attrs={"readonly":"readonly", "style":"background-color:white; border: 1px solid #ced4da;"})
        }