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


import cx_Oracle
import json
import datetime
import pytz
import pendulum
import uuid


from .models import (
    Event
)
from .forms import (
    ExportForm,
    BrandSqlForm
)

from django.core.mail import send_mail

api_key = "AIzaSyDaSaYxmAODxk7k9Eq3GjXKsRz6WtxQ9OE"
api_secret = 'cc829454d5577aaedd60995158989389'
api_token = '410463a6b39dcac621e5c9115dad56a3'

def update_mixpanel(from_date, to_date):
    r = requests.get('https://data.mixpanel.com/api/2.0/export/?from_date={}&to_date={}'.format(from_date, to_date), auth=(api_secret, api_token))
    content = r.content
    decoded_content = (content.decode("utf-8"))
    # for line in decoded_content.splitlines():
    #     print (line)
    return decoded_content

class AboutView(generic.ListView):

    template_name = "home/home.html"


    def get_queryset(self):

        return "hi"


class HomeView(generic.ListView):

    template_name = "events/user_home.html"


    def get_queryset(self):

        return "hi"


def export_mixpanel(request):
    # if this is a POST request we need to process the form data

    if request.method == "POST":
        form = ExportForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            r = requests.get('https://data.mixpanel.com/api/2.0/export/?from_date={}&to_date={}'.format(cd['from_date'], cd['to_date']), auth=(api_secret, api_token))
            content = r.content
            decoded_content = (content.decode("utf-8"))
        else:
            print(form)
        # create a form instance and populate it with data from the request:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="MixPanel.csv"'

        writer = csv.writer(response)
        writer.writerow(['Event', 'Time', 'Distinct ID', 'Insert ID', 'Functionality', 'Row Count', 'mp_lib', 'Hierarchy', 'Org Node Value', 'Selected Org Node Type', 'Tab Selected'])
        data=[]
        for line in decoded_content.splitlines():
            data.append(json.loads(line))

        for item in data:
            print(item)
            hierarchy = ''
            org_value = ''
            org_node_type = ''
            tab_selected = ''


            if 'Hierarchy' in item['properties']:
                hierarchy = item['properties']['Hierarchy']
            if 'Org Node Value' in item['properties']:
                org_value = item['properties']['Org Node Value']
            if 'Selected Org Node' in item['properties']:
                org_node_type = item['properties']['Selected Org Node']
            if 'Tab Selected' in item['properties']:
                tab_selected = item['properties']['Tab Selected']

            writer.writerow([item['event'],item['properties']['time'],item['properties']['distinct_id'],item['properties']['$insert_id'],item['properties']['Functionality'],item['properties']['Row Count'],item['properties']['mp_lib'],hierarchy,org_value, org_node_type, tab_selected])

        return response


    # if a GET (or any other method) we'll create a blank form
    else:
        form = ExportForm()
        print("ELSE")

    context = {
        "title": "MixPanel Data Exporter",
        "form": form,
        }
    return render(request, "events/export.html", context)


def create_brand_sql(request):
    # if this is a POST request we need to process the form data

    if request.method == "POST":
        form = BrandSqlForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            name = cd['name']
        else:
            print(form)
        # create a form instance and populate it with data from the request:

        if "'" in name:
            name = name.replace("'", "''")

        content = """USE Atlas;
GO

DECLARE
    @UserName varchar(128) = 'kotten-joseph@aramark.com'
    ,@BrandTypeID int = {}
    ,@BrandName varchar(128) = '{}'
    ,@BrandCategoryID int = {}
    ,@BrandStatusID int = 1
    ,@ImportWorksheet bit = 0
    ,@ReportIntervalID int = 1
    ,@RoyaltyPaymentReportTypeID int = 2
    ,@SendCalendarMonthSalesSummary bit = 0
    ,@AllowStoreCutoff bit = 0
    ,@FoodCostLowerPercent float = 0.0
    ,@FoodCostUpperPercent float = 0.0
    ,@LaborCostLowerPercent float = 0.0
    ,@LaborCostUpperPercent float = 0.0
    ,@OracleConcept char(4) = '{}'


DECLARE @UserID		INT
    --get the userid based on the passed in username
EXEC GetUserIdByName @UserName, @UserID OUTPUT


INSERT INTO [RetailBrands].[Brand]
        (BrandTypeID
        ,BrandName
        ,BrandCategoryID
        ,BrandStatusID
        ,ImportWorksheet
        ,ReportIntervalID
        ,RoyaltyPaymentReportTypeID
        ,SendCalendarMonthSalesSummary
        ,AllowStoreCutoff
        ,ModifiedBy
        ,DateLastModified
        ,FoodCostLowerPercent
        ,FoodCostUpperPercent
        ,LaborCostLowerPercent
        ,LaborCostUpperPercent
        ,OracleConcept
        )
        VALUES
        ( @BrandTypeID
        ,@BrandName
        ,@BrandCategoryID
        ,@BrandStatusID
        ,@ImportWorksheet
        ,@ReportIntervalID
        ,@RoyaltyPaymentReportTypeID
        ,@SendCalendarMonthSalesSummary
        ,@AllowStoreCutoff
        ,@UserID
        ,GETUTCDATE()
        ,@FoodCostLowerPercent
        ,@FoodCostUpperPercent
        ,@LaborCostLowerPercent
        ,@LaborCostUpperPercent
        ,@OracleConcept
        )

SELECT  SCOPE_IDENTITY() [BrandIDReturn];""".format(cd['brand_type'], name, cd['brand_cat'], cd['concept'])

        response = HttpResponse(content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename={}'.format(cd['name'] + ".sql")
        return response


    # if a GET (or any other method) we'll create a blank form
    else:
        form = BrandSqlForm()
        print("ELSE")
    concepts = [
            ["1","Asian","7003"],
            ["37","Authentic / Ethnic","9504"],
            ["2","Bakery Cafe","3061"],
            ["44","BBQ","1210"],
            ["15","Beverage","1215"],
            ["16","Breakfast",""],
            ["38","Burger / Grill","1120"],
            ["18","Casual","1210"],
            ["4","Chicken","1095"],
            ["5","Coffee","1514"],
            ["39","Convenience","9503"],
            ["21","Dessert / Smoothie / Yogurt","5001"],
            ["40","Healthy","9502"],
            ["12","Impulse at Register","1220"],
            ["7","Mexican","3006"],
            ["8","Other",""],
            ["41","Pizza / Italian","1105"],
            ["23","Residential",""],
            ["10","Sandwich","3005"],
            ["43","SeaFood",""],
            ["11","Snack","9510"],
            ]

    context = {
    "title": "Brand SQL Generator",
    "form": form,
    "concepts": concepts
    }

    return render(request, "events/export.html", context)

