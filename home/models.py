import datetime
import pytz
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
from bootstrap_datepicker_plus import DateTimePickerInput, DatePickerInput
from django.contrib.auth.models import User

# Create your models here.

class Page(models.Model):
    page_title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='thesippelfarm', null=True, default=None, blank=True)
    photo_title = models.CharField(max_length=200, null=True, default=None, blank=True)
    content_title = models.CharField(max_length=200, null=True, default=None, blank=True)
    content_text = models.TextField(null=True, default=None, blank=True)
    order = models.IntegerField(null=True, default=None, blank=True)
    published = models.BooleanField()

    def __str__(self):
        return "{}: Pub: {}".format(self.page_title, self.published)

class PageContent(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='thesippelfarm', null=True, default=None, blank=True)
    photo_title = models.CharField(max_length=200, null=True, default=None, blank=True)
    content_title = models.CharField(max_length=200, null=True, default=None, blank=True)
    content_text = models.TextField(null=True, default=None, blank=True)
    order = models.IntegerField(null=True, default=None, blank=True)
    published = models.BooleanField()

    def __str__(self):
        return "{}: {}- Pub: {}".format(self.page, self.order, self.published)

class ForSaleItems(models.Model):
    photo = models.ImageField(upload_to='thesippelfarm', null=True, default=None, blank=True)
    content_title = models.CharField(max_length=200, null=True, default=None, blank=True)
    content_text = models.TextField(null=True, default=None, blank=True)
    order = models.IntegerField(null=True, default=None, blank=True)
    published = models.BooleanField()

    def __str__(self):
        return "{}: {}- Pub: {}".format(self.content_title, self.order, self.published)
