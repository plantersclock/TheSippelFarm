from django import forms

from django.contrib.admin import widgets

from bootstrap_datepicker_plus import DateTimePickerInput, DatePickerInput
from django.contrib.admin import widgets

import datetime

brand_type_choices = [
    ("8", "Local (8)"),
    ("10", "Regional (10)"),
    ("11", "Proprietary (11)"),
    ("12", "National (12)"),
]

brand_cat_choices =[
    ( "1", "Asian (1)"),
    ( "37", "Authentic / Ethnic - 37)"),
    ( "2", "Bakery Cafe (2)"),
    ( "44", "BBQ (44)"),
    ( "15", "Beverage (15)"),
    ( "16", "Breakfast (16)"),
    ( "3", "Burger (3)"),
    ( "38", "Burger / Grill (38)"),
    ( "18", "Casual (18)"),
    ( "19", "Catering - CaterTrax (19)"),
    ( "27", "Catering - Manual (27)"),
    ( "4", "Chicken (4)"),
    ( "5", "Coffee (5)"),
    ( "20", "Comfort (20)"),
    ( "39", "Convenience (39)"),
    ( "17", "C-Store (17)"),
    ( "21", "Dessert / Smoothie / Yogurt (21)"),
    ( "29", "Exhibition (29)"),
    ( "40", "Healthy (40)"),
    ( "12", "Impulse at Register (12)"),
    ( "6", "Italian (6)"),
    ( "36", "Mediterranean (36)"),
    ( "7", "Mexican (7)"),
    ( "8", "Other (8)"),
    ( "34", "Oven (34)"),
    ( "9", "Pizza (9)"),
    ( "41", "Pizza / Italian (41)"),
    ( "23", "Residential (23)"),
    ( "32", "Salad (32)"),
    ( "10", "Sandwich (10)"),
    ( "43", "SeaFood (43)"),
    ( "11", "Snack (11)")
]

class ExportForm(forms.Form):
    from_date = forms.DateField(label='From Date:', widget=DatePickerInput())
    to_date = forms.DateField(label='To Date:', widget=DatePickerInput())


class BrandSqlForm(forms.Form):
    name = forms.CharField(label='Brand Name')
    brand_type = forms.ChoiceField(label='Brand Type', choices=brand_type_choices)
    brand_cat = forms.ChoiceField(label='Brand Category', choices=brand_cat_choices)
    concept = forms.CharField(label='Concept', max_length=200)

