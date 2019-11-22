from django import forms

from django.contrib.admin import widgets

from bootstrap_datepicker_plus import DateTimePickerInput, DatePickerInput
from django.contrib.admin import widgets

import datetime

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
